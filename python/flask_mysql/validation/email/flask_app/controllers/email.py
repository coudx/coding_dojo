from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.email import Email


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if not Email.validate_email(request.form):
        return redirect("/")
    Email.insert(request.form["email"])
    return redirect("/success")


@app.route("/success")
def success():
    return render_template(
        "success.html", last=Email.get_last()[0], data=Email.get_all()
    )
