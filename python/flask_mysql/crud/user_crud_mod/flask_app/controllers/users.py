from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.users import Users


@app.route("/")
def index():
    return redirect("/users")


@app.route("/users")
def read():
    print(Users.get_all())
    return render_template("read.html", data=Users.get_all())


@app.route("/users/new", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("create.html")
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    Users.add(data)
    return redirect("/users")


@app.route("/users/<id>")
def view(id):
    print(Users.get(id))
    return render_template("view.html", data=Users.get(id)[0])


@app.route("/users/<id>/edit", methods=["POST", "GET"])
def edit(id):
    if request.method == "GET":
        return render_template("edit.html", data=Users.get(id)[0])
    data = {
        "id": id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    Users.update(data)
    return redirect("/users/" + str(id))


@app.route("/users/<id>/delete")
def delete(id):
    Users.delete(id)
    return redirect("/users")
