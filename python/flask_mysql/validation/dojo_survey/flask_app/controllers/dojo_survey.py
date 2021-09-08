from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.survey import Survey


@app.route("/")
def survey():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    if not Survey.validate_survey(request.form):
        return redirect("/")
    Survey.insert(request.form)
    return redirect("/result")


@app.route("/result")
def result():
    return render_template("result.html", data=Survey.get_last_survey()[0])
    # return session.get("survey")
