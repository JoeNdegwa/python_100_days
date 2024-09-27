""" main python file """
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB with the UserMixin

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    phone: Mapped[str] = mapped_column(String(15), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    firstname: Mapped[str] = mapped_column(String(1000))
    lastname: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            phone=request.form.get('phone'),
            password=hash_and_salted_password,
            firstname=request.form.get('firstname'),
            lastname=request.form.get('lastname')
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        # Email doesn't exist or password incorrect.
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html")


# Only logged-in users can access the route
@app.route('/secrets')
@login_required
def secrets():
    print(current_user.firstname)
    # Passing the name from the current_user
    return render_template("secrets.html", name=current_user.firstname)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# Only logged-in users can down download the pdf
@app.route('/download', methods=['POST'])
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)

""" base html file
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>MAIN Portal</title>
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/styles.css')}}"
    />
  </head>

  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="/">MAIN</a>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="{{ url_for('home') }}">Home</a>
          </li>
          <!-- TODO: Hide the Login/Registration navigation for logged-in users -->
          {% if not logged_in: %}
          <li class="nav-item">
            <a class="nav-link" href="{{ url_for('login') }}">Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{{ url_for('register') }}">Register</a>
          </li>
          {% endif %}
          <li class="nav-item">
            <a class="nav-link" href="{{ url_for('logout') }}">Log Out</a>
          </li>
        </ul>
      </div>
    </nav>
    {% block content %} {% endblock %}
  </body>
</html>

"""
""" index html file 
{% extends "base.html" %} {% block content %}

<div class="box">
  <h1>Main Portal</h1>
  <!-- TODO: Hide the Login/Registration buttons for logged-in users -->
  <a href="{{ url_for('login') }}" class="btn btn-primary btn-block btn-large"
    >Login</a
  >
  <a
    href="{{ url_for('register') }}"
    class="btn btn-secondary btn-block btn-large"
    >Register</a
  >
</div>

{% endblock %}

"""
""" login html file 
{% extends "base.html" %}
{% block content %}

<div class="box">
    <h1>Login</h1>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        {% for message in messages %}
         <p>{{ message }}</p>
        {% endfor %}
      {% endif %}
    {% endwith %}
    <form method="post">
        <input type="text" name="email" placeholder="Email" required="required"/>
        <input type="password" name="password" placeholder="Password" required="required"/>
        <button type="submit" class="btn btn-primary btn-block btn-large">LOGIN</button>
    </form>
</div>

{% endblock %}

"""
""" secrets html file
{% extends "base.html" %} {% block content %}

<!--TODO: Display the user's name in the h1 title-->
<div class="container">
  <h1 class="title">Welcome, {{ name }}</h1>
  <!--TODO: Make a GET request to the /download path-->
  <a href="#">Download Your File</a>
</div>
{% endblock %}

"""
""" register html file
{% extends "base.html" %}
{% block content %}

<div class="box">
	<h1>Register</h1>
    <form action="{{ url_for('register') }}" method="post">
    	<input type="text" name="firstname" placeholder="First Name" required="required" />
        <input type="text" name="lastname" placeholder="Last Name" required="required" />
        <input type="text" name="phone" placeholder="0700100200" required="required" />
		<input type="email" name="email" placeholder="Email" required="required" />
        <input type="password" name="password" placeholder="Password" required="required" />
        <button type="submit" class="btn btn-primary btn-block btn-large">SIGN UP</button>
    </form>
</div>

{% endblock %}

"""
