from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "x"


@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
    return render_template(
        "index.html", gold=session.get("gold"), log=session.get("log")
    )


@app.route("/process_money", methods=["POST"])
def process():
    logtime = datetime.now()
    formatedTime = logtime.strftime("%y/%m/%d %I:%M %p")
    if int(request.form["gamble"]):
        session["gain"] = random.randint(0, 1)
    else:
        session["gain"] = 1
    gold = random.randint(int(request.form["lo"]), int(request.form["hi"]))
    session["gold"] = gold + session.get("gold")
    if session.get("gain"):
        if "log" not in session:
            session["log"] = ""
        session["log"] = (
            "<p style='color: green;'>Earned "
            + str(gold)
            + " golds from the "
            + request.form["act"]
            + "! "
            + formatedTime
            + "</p>"
            + session.get("log")
        )
    else:
        session["log"] = (
            "<p style='color: red;'>Entered a casino and lost "
            + str(gold)
            + " golds... Ouch. "
            + formatedTime
            + "</p>"
            + session.get("log")
        )
    return redirect("/")


@app.route("/reset")
def reset():
    session.pop("log")
    session.pop("gold")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
