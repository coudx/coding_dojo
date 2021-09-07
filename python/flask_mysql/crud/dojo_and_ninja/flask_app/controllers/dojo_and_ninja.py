from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/")
def index():
    return redirect("/dojos")


@app.route("/dojos", methods=["POST", "GET"])
def dojo():
    if request.method == "GET":
        return render_template("dojo.html", data=Dojo.get_all())
    Dojo.add(request.form["name"])
    return redirect("/dojos")


@app.route("/ninjas", methods=["POST", "GET"])
def ninja():
    if request.method == "GET":
        return render_template("ninja.html", data=Dojo.get_all())
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"],
    }
    Ninja.add(data)
    return redirect("/dojos")


@app.route("/dojos/<n>")
def read(n):
    return render_template("read.html", data=Dojo.get_dojo_with_ninja(n))
