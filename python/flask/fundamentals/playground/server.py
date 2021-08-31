from flask import Flask, render_template

app = Flask(__name__)


@app.route("/play")
def index():
    return render_template("index.html", num=4, classes="bg-info")


@app.route("/play/<x>")
def num(x):
    return render_template("index.html", num=int(x), classes="bg-info")


# too much work to write every color with css
# # @app.route("/play/<x>/<color>")
# def color(x, color):
#     return render_template("index.html", num=int(x), classes=color)


if __name__ == "__main__":
    app.run(debug=True)
