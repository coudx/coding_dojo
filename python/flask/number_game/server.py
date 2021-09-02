from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "x"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "hof" in session:
            session["hof"].append(request.form["name"])
        else:
            session["hof"] = []
        session.pop("num")
        session.pop("guess")
        session.pop("counter")
        return redirect("/")
    if "num" in session:
        if "guess" in session:
            if session.get("guess") > session.get("num"):
                data = {
                    "string": "Too High!",
                    "color": "bg-danger text-white",
                    "win": "hide",
                    "lose": "hide",
                }
            elif session.get("guess") < session.get("num"):
                data = {
                    "string": "Too Low!",
                    "color": "bg-danger text-white",
                    "win": "hide",
                    "lose": "hide",
                }
            else:
                data = {
                    "string": str(session.get("guess")) + " was the number!",
                    "color": "bg-success text-white",
                    "display": "hide",
                    "guess": "hide",
                    "lose": "hide",
                }
        else:
            data = {
                "string": "",
                "color": "",
                "display": "hide",
                "win": "hide",
                "lose": "hide",
            }
    else:
        session["num"] = random.randint(1, 100)
        data = {"display": "hide", "win": "hide", "lose": "hide"}
    if "counter" in session:
        if session.get("counter") == 5:
            data = {"display": "hide", "win": "hide", "guess": "hide"}
    return render_template("index.html", value=data)


@app.route("/guess", methods=["POST"])
def guess():
    session["guess"] = int(request.form["gnum"])
    if "counter" in session:
        session["counter"] = session.get("counter") + 1
    else:
        session["counter"] = 1
    return redirect("/")


@app.route("/winners")
def hof():
    return render_template("winners.html", hof=session.get("hof"))


@app.route("/lose", methods=["POST"])
def lose():
    session.pop("num")
    session.pop("guess")
    session.pop("counter")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
