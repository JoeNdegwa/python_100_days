"""Main server file"""
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length 
from flask_bootstrap import Bootstrap5 


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
  
"""index html file
{% extends "base.html" %}
{% block title %}Secrets{% endblock %}
{% block content %}
<!--Using Boostrap classes for styling here-->
<div class="jumbotron">
	<div class="container">
		<h1>Welcome</h1>
		<p>Are you ready to discover my secret?</p>
		<a class="btn btn-primary btn-lg" href=" {{ url_for('login') }} ">Login</a>
	</div>
</div>
{% endblock %}
"""

"""
base html file
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    {% block styles %}
        <!-- Bootstrap CSS -->
        {{ bootstrap.load_css() }}
    {% endblock %}

    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}

</body>
</html>
"""

"""
login html file

{% extends "base.html" %}
{% from 'bootstrap5/form.html' import render_form %}
{% block title %}Login{% endblock %}
{% block content %}
    <div class="container">
    <h1>Login</h1>
        {{ render_form(form) }}
    </div>
{% endblock %}

"""

"""
success html file

{% extends "base.html" %}
{% block title %}Access Granted{% endblock %}
{% block content %}
	<div class="container">
		<h1>Top Secret </h1>
		<iframe src="https://giphy.com/embed/Ju7l5y9osyymQ" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
		<p><a href="https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ">via GIPHY</a></p>
	</div>
{% endblock %}
"""

"""
denied html file

{% extends "base.html" %}
{% block title %}Access Denied{% endblock %}
{% block content %}
	<div class="container">
		<h1>Access Denied </h1>
		<iframe src="https://giphy.com/embed/1xeVd1vr43nHO" width="480" height="271" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
		<p><a href="https://giphy.com/gifs/cheezburger-funny-dog-fails-1xeVd1vr43nHO">via GIPHY</a></p>
	</div>
{% endblock %}

"""
