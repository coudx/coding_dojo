from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.authors import Author
from flask_app.models.books import Book
from flask_app.models.favorite import Fav


@app.route("/")
def index():
    return redirect("/authors")


@app.route("/authors", methods=["GET", "POST"])
def author():
    if request.method == "GET":
        print(Author.get_all())
        return render_template("authors.html", data=Author.get_all())
    print(request.form["name"])
    Author.insert(request.form["name"])
    return redirect("/authors")


@app.route("/books", methods=["GET", "POST"])
def book():
    if request.method == "GET":
        return render_template("books.html", data=Book.get_all())
    data = {"title": request.form["title"], "page": int(request.form["page"])}
    Book.insert(data)
    return redirect("/books")


@app.route("/<x>/<y>", methods=["GET", "POST"])
def books(x, y):
    if request.method == "GET":
        if x == "books":
            datas = {
                "name": Book.get(int(y))[0]["title"],
                "fav": Fav.get_author_fav_the_book(int(y)),
                "data": Author.get_rest(int(y)),
            }
            return render_template("b-show.html", data=datas)
        if x == "authors":
            datas = {
                "name": Author.get(int(y))[0]["name"],
                "fav": Fav.get_book_fav_by_author(int(y)),
                "data": Book.get_rest(int(y)),
            }
            return render_template("a-show.html", data=datas)
    if x == "books":
        id = {"books": int(y), "authors": int(request.form["id"])}
    if x == "authors":
        id = {"authors": int(y), "books": int(request.form["id"])}
    Fav.insert(id)
    return redirect("/" + x + "/" + y)
