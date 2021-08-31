from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/dojo")
def dojo():
    return "DOjo!"


@app.route("/say/<str>")
def say(str):
    return str


@app.route("/repeat/<num>/<str>")
def repeat(num, str):
    page = ""
    for x in range(int(num)):
        page += f"<h1>{str}</h1>"
    return page


@app.errorhandler(404)
def handle404(e):
    return "Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug=True)
