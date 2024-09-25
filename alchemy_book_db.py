""" main file """
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)

# CREATE DATABASE

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit_rating.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

""" index html file
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Library</title>
  </head>
  <body>
    <h1>My Library</h1>
    {% if books == []: %}
    <p>Library is empty.</p>
    {% endif %}
    <ul>
      {% for book in books %}
      <li>
        <a href="{{ url_for('delete', id=book.id) }}">Delete</a>
        {{book.title}} - {{book.author}} - {{book.rating}}/10
        <a href="{{ url_for('edit', id=book.id) }}">Edit Rating</a>
      </li>
      {% endfor %}
    </ul>
    <a href="{{ url_for('add') }}">Add New Book</a>
  </body>
</html>
"""

""" add html file
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Add Book</title>
  </head>
  <body>
    <form action="{{ url_for('add') }}" method="POST">
      <label>Book Name</label>
      <input name="title" type="text" />
      <label>Book Author</label>
      <input name="author" type="text" />
      <label>Rating</label>
      <input name="rating" type="text" />
      <button type="submit">Add Book</button>
    </form>
  </body>
</html>
"""

""" edit rating html file

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Edit Rating</title>
  </head>
  <body>
    <form action="{{ url_for('edit') }}" method="POST">
      <p>Book Name: {{book.title}}</p>
      <p>Current Rating {{book.rating}}</p>
      <input hidden="hidden" name="id" value="{{book.id}}" />
      <input name="rating" type="text" placeholder="New Rating" />
      <button type="submit">Change Rating</button>
    </form>
  </body>
</html>
"""
