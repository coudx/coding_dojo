from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route("/")
def index():
    if "id" in session:
        return redirect("/dashboard")
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    if not User.regValid(request.form):
        return redirect("/")
    session["id"] = User.insert(request.form)
    return redirect("/dashboard")


@app.route("/login", methods=["POST"])
def login():
    if not User.loginValid(request.form):
        return redirect("/")
    session["id"] = User.loginValid(request.form)
    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():
    if "id" not in session or not session.get("id"):
        session.clear()
        return redirect("/")
    data = {
        "user": User.get_by_id(session.get("id")),
        "recipe": Recipe.get_all_by_uid(session.get("id")),
    }
    return render_template("dashboard.html", data=data)


@app.route("/dashboard/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/dashboard/addrecipe", methods=["POST", "GET"])
def add():
    if "id" not in session or not session.get("id"):
        session.clear()
        return redirect("/")
    print(request.form)
    if request.method == "GET":
        return render_template("addrecipe.html", data=User.get_by_id(session.get("id")))
    if not Recipe.valid(request.form):
        return redirect("/dashboard/addrecipe")
    recipe_id = Recipe.add(Recipe.parseData(session.get("id"), request.form))
    return redirect("/dashboard/recipe/" + str(recipe_id))


@app.route("/dashboard/recipe/<x>")
def recipe(x):
    if "id" not in session or not session.get("id"):
        session.clear()
        return redirect("/")
    data = {"id": x, "user_id": session.get("id")}
    if Recipe.validUser(data):
        cb_data = {
            "user": User.get_by_id(data["user_id"]),
            "recipe": Recipe.get_detail(data["id"]),
        }
        return render_template("recipe.html", data=cb_data)
    return redirect("/danger")


@app.route("/dashboard/recipe/<x>/edit", methods=["POST", "GET"])
def edit(x):
    data = {"id": int(x), "user_id": session.get("id")}
    if Recipe.validUser(data):
        if request.method == "GET":
            cb_data = {
                "user": User.get_by_id(data["user_id"]),
                "recipe": Recipe.get_detail(data["id"]),
            }
            return render_template("editrecipe.html", data=cb_data)
        else:
            if not Recipe.valid(request.form):
                return redirect("/dashboard/recipe/" + x + "/edit")
            else:
                Recipe.update(Recipe.parseData(data["user_id"], request.form))
                return redirect("/dashboard/recipe/" + x)
    return redirect("/danger")


@app.route("/dashboard/recipe/<x>/delete")
def delete(x):
    data = {"id": int(x), "user_id": session.get("id")}
    if Recipe.validUser(data):
        Recipe.delete(data["id"])
        return redirect("/dashboard")
    return redirect("/danger")


@app.route("/danger")
def warning():
    session.clear()
    return render_template("warning.html", ip=request.remote_addr)
