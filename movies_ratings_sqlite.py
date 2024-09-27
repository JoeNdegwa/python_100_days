""" main python file """
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# Global variables
MOVIE_DB_API_KEY = "USE_YOUR_OWN_CODE"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# Initialize the app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# Create DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Create Table
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g 8.0")
    review = StringField("Your Review")
    submit = SubmitField("Done")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    # Convert ScalarResult to Python list
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={
            "api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.hml", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

""" base html file
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />

    {% block styles %}
    <!-- Load Bootstrap-Flask CSS here -->
    {{ bootstrap.load_css() }}
    <!-- Link to the styles.css here to apply styling to all the child templates.-->
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700"
    />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css?family=Poppins:300,400,700"
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
      integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog=="
      crossorigin="anonymous"
    />
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/styles.css') }}"
    />
    {% endblock %}

    <title>{% block title %}{% endblock %}</title>
  </head>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>
"""

""" index html file
{% extends 'base.html' %}


{% block title %}My Top 10 Movies{% endblock %}

{% block content %}
<div class="container">
  <h1 class="heading">My Top 10 Movies</h1>
  <p class="description">These are my all-time favourite movies.</p>
    {% for movie in movies %}
  <div class="card" >
    <div class="front" style="background-image: url('{{movie.img_url}}');">
        <p class="large">{{ movie.ranking }}</p>
    </div>
    <div class="back">
      <div>
    <div class="title">{{movie.title}} <span class="release_date">({{movie.year}})</span></div>
        <div class="rating">
            <label>{{movie.rating}}</label>
          <i class="fas fa-star star"></i>
        </div>
          <p class="review">"{{movie.review}}"</p>
        <p class="overview">{{movie.description}}</p>

        <a href="{{ url_for('rate_movie', id=movie.id) }}" class="button">Update</a>
        <a href="{{ url_for('delete_movie', id=movie.id) }}" class="button delete-button">Delete</a>

      </div>
    </div>
  </div>
    {% endfor %}
</div>
<div class="container text-center add">
<a href="{{ url_for('add_movie') }}" class="button">Add Movie</a>
</div>

{% endblock %}
"""
""" select html file
{% extends 'base.html' %}

{% block title %}Select Movie{% endblock %}

{% block content %}
<div class="container">
    <h1 class="heading">Select Movie</h1>
    {% for movie in options: %}
  <p>
    <a href="{{ url_for('find_movie', id=movie.id) }} ">{{ movie.title }} - {{movie.release_date}}</a>
  </p>
  {% endfor %}

</div>
{% endblock %}
"""
""" add html file
{% extends 'base.html' %}
{% from 'bootstrap5/form.html' import render_form %}

{% block title %}Add Movie{% endblock %}

{% block content %}
<div class="content">
    <h1 class="heading">Add a Movie</h1>
    {{ render_form(form, novalidate=True) }}
</div>
{% endblock %}
"""
"" styles css file

*, *:before, *:after {
	 box-sizing: border-box;
}
 html {
	 font-size: 18px;
	 line-height: 1.5;
	 font-weight: 300;
	 color: #333;
	 font-family: "Nunito Sans", sans-serif;
}
 body {
	 margin: 0;
	 padding: 0;
	 height: 100vh;
	 background-color: #ecf0f9;
	 background-attachment: fixed;
}
.large {
     font-size: 3rem;
}
 .content {
	 display: flex;
	 margin: 0 auto;
	 justify-content: center;
	 align-items: center;
	 flex-wrap: wrap;
	 max-width: 1500px;
}
 p.overview {
	 font-size: 12px;
	 height: 200px;
	 width: 100%;
	 overflow: hidden;
	 text-overflow: ellipsis;
}
 .heading {
	 width: 100%;
	 margin-left: 1rem;
	 font-weight: 900;
	 font-size: 1.618rem;
	 text-transform: uppercase;
	 letter-spacing: 0.1ch;
	 line-height: 1;
	 padding-bottom: 0.5em;
	 margin-bottom: 1rem;
	 position: relative;
}
 .heading:after {
	 display: block;
	 content: '';
	 position: absolute;
	 width: 60px;
	 height: 4px;
	 background: linear-gradient(135deg, #1a9be6, #1a57e6);
	 bottom: 0;
}
 .description {
	 width: 100%;
	 margin-top: 0;
	 margin-left: 1rem;
	 margin-bottom: 3rem;
}
 .card {
	 color: inherit;
	 cursor: pointer;
	 width: calc(33% - 3rem);
	 min-width: calc(33% - 3rem);
	 height: 400px;
	 min-height: 400px;
	 perspective: 1000px;
	 margin: 1rem auto;
	 position: relative;
}
 @media screen and (max-width: 800px) {
	 .card {
		 width: calc(50% - 3rem);
	}
}
 @media screen and (max-width: 500px) {
	 .card {
		 width: 100%;
	}
}
 .front, .back {
	 display: flex;
	 border-radius: 6px;
	 background-position: center;
	 background-size: cover;
	 text-align: center;
	 justify-content: center;
	 align-items: center;
	 position: absolute;
	 height: 100%;
	 width: 100%;
	 -webkit-backface-visibility: hidden;
	 backface-visibility: hidden;
	 transform-style: preserve-3d;
	 transition: ease-in-out 600ms;
}
 .front {
	 background-size: cover;
	 padding: 2rem;
	 font-size: 1.618rem;
	 font-weight: 600;
	 color: #fff;
	 overflow: hidden;
	 font-family: Poppins, sans-serif;
}
 .front:before {
	 position: absolute;
	 display: block;
	 content: '';
	 top: 0;
	 left: 0;
	 right: 0;
	 bottom: 0;
	 background: linear-gradient(135deg, #1a9be6, #1a57e6);
	 opacity: 0.25;
	 z-index: -1;
}
 .card:hover .front {
	 transform: rotateY(180deg);
}
 .card:nth-child(even):hover .front {
	 transform: rotateY(-180deg);
}
 .back {
	 background: #fff;
	 transform: rotateY(-180deg);
	 padding: 0 2em;
}
 .card:hover .back {
	 transform: rotateY(0deg);
}
 .card:nth-child(even) .back {
	 transform: rotateY(180deg);
}
 .card:nth-child(even):hover .back {
	 transform: rotateY(0deg);
}
 .button {
	 transform: translateZ(40px);
	 cursor: pointer;
	 -webkit-backface-visibility: hidden;
	 backface-visibility: hidden;
	 font-weight: bold;
	 color: #fff;
	 padding: 0.5em 1em;
	 border-radius: 100px;
	 font: inherit;
	 background: linear-gradient(135deg, #1a9be6, #1a57e6);
	 border: none;
	 position: relative;
	 transform-style: preserve-3d;
	 transition: 300ms ease;
}
 .button:before {
	 transition: 300ms ease;
	 position: absolute;
	 display: block;
	 content: '';
	 transform: translateZ(-40px);
	 -webkit-backface-visibility: hidden;
	 backface-visibility: hidden;
	 height: calc(100% - 20px);
	 width: calc(100% - 20px);
	 border-radius: 100px;
	 left: 10px;
	 top: 16px;
	 box-shadow: 0 0 10px 10px rgba(26, 87, 230, 0.25);
	 background-color: rgba(26, 87, 230, 0.25);
}

.button.delete-button {
	 background-color: rgba(230, 87, 230, 0.25);
	 background: linear-gradient(135deg, #e61a46, #e61a1a);
}
.button.delete-button:before {
	 background-color: rgba(230, 87, 230, 0.25);
	 box-shadow: 0 0 10px 10px rgba(230, 87, 230, 0.25);
}
 .button:hover {
	 transform: translateZ(55px);
}
 .button:hover:before {
	 transform: translateZ(-55px);
}
 .button:active {
	 transform: translateZ(20px);
}
 .button:active:before {
	 transform: translateZ(-20px);
	 top: 12px;
	 top: 12px;
}
.container.add {
    margin-top: 40px;
    margin-bottom: 20px;
}
.rating {
    color: #E4BB23;
}
.review {
    font-style: italic;
}
 .movie_gens {
	 font-size: 11.5px;
}
 .title {
	 font-weight: bold;
}
 .release_date {
	 font-weight: normal;
}

"""
