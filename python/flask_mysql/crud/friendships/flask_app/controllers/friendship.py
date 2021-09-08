from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import User
from flask_app.models.friendship import Friendship


@app.route("/")
def index():
    return redirect("/friendships")


@app.route("/friendships", methods=["GET", "POST"])
def friendship():
    if request.method == "GET":
        return render_template(
            "index.html", data=Friendship.get_all(), user=User.get_all_user_fullname()
        )
    data = {
        "user_id": int(request.form["user_id"]),
        "friend_id": int(request.form["friend_id"]),
    }
    Friendship.insert(data)
    return redirect("/friendships")


@app.route("/adduser", methods=["POST"])
def adduser():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
    }
    User.insert(data)
    return redirect("/friendships")
