from flask import Flask, render_template, request, redirect
from users import Users

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
