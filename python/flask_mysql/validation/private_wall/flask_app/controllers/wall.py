from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.message import Message

bcrypt = Bcrypt(app)


@app.route("/")
def index():
    if "data" in session:
        return redirect("/dashboard")
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
    session["data"] = User.get_by_id(User.insert(data))
    return redirect("/dashboard")


@app.route("/login", methods=["POST"])
def login():
    data = {"username": request.form["username"]}
    user = User.get(data)
    if not user:
        flash("Invalid Username/Password Combination", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user["password"], request.form["password"]):
        flash("Invalid Username/Password Combination", "login")
        return redirect("/")
    session["data"] = User.getuser(data)
    return redirect("/dashboard")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        pass_data = {
            "content": request.form["content"],
            "user_id": request.form["user_id"],
            "sender": session.get("data")["first_name"]
            + " "
            + session.get("data")["last_name"],
            "sender_id": session.get("data")["id"],
        }
        Message.insert(pass_data)
        return redirect("/dashboard")
    if "data" not in session:
        return redirect("/")
    data = session.get("data")
    users = User.get_userlist(data["id"])
    messages = Message.get_message(data["id"])
    length = len(messages)
    if not Message.get_num_message_sent(data["id"]):
        num = 0
    else:
        num = Message.get_num_message_sent(data["id"])
    return render_template(
        "dashboard.html", data=data, user=users, len=length, num=num, message=messages
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/delete/<x>")
def delete(x):
    if session.get("data")["id"] != Message.filter(x):
        return redirect("/danger")
    Message.delete(x)
    return redirect("/dashboard")


@app.route("/danger")
def danger():
    session.clear()
    return render_template("danger.html", ip=request.remote_addr)
