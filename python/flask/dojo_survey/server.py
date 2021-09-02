from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "x"


@app.route("/")
def survey():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    session["survey"] = request.form
    return redirect("/result")


@app.route("/result")
def result():
    return render_template("result.html", data=session.get("survey"))
    # return session.get("survey")


if __name__ == "__main__":
    app.run(debug=True)
