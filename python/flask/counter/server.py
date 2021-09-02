from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "0"


@app.route("/")
def index():
    if "count" in session:
        session["count"] = session.get("count") + 1
    else:
        session["count"] = 1
    if "visit" in session:
        session["visit"] = session.get("visit") + 1
    else:
        session["visit"] = 1
    return render_template(
        "index.html", ct=session.get("count"), visit=session.get("visit")
    )


@app.route("/destroy_session")
def reset():
    session.clear()
    return redirect("/")


@app.route("/plus", methods=["POST"])
def plus():
    session["count"] = session.get("count") + int(request.form["num"]) - 1
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
