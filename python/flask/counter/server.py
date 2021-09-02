from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "0"


@app.route("/", methods=["POST", "GET"])
def index():
    if "count" in session:
        session["count"] = session.get("count") + 1
    else:
        session["count"] = 1
    return render_template("index.html", ct=session.get("count"))


@app.route("/destroy_session")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
