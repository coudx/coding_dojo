from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

bcrypt = Bcrypt(app)


@app.route("/")
def index():
    session.clear()
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    if not User.validUser(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print(pw_hash)
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "username": request.form["username"],
        "password": pw_hash,
    }
    print(data)
    session["data"] = User.get_by_id(User.insert(data))[0]
    return redirect("/dashboard")


@app.route("/login", methods=["POST"])
def login():
    data = {"username": request.form["username"]}
    user = User.get(data)[0]
    if not user:
        flash("Invalid Username/Password Combination", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user["password"], request.form["password"]):
        flash("Invalid Username/Password Combination", "login")
        return redirect("/")
    session["data"] = user
    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", data=session.get("data"))
