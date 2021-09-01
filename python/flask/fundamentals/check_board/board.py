from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def default():
    return render_template("index.html", x=4, y=4, color1="white", color2="black")


@app.route("/<n>")
def sized(n):
    return render_template(
        "index.html", x=int(int(n) / 2), y=int(int(n) / 2), color1="red", color2="green"
    )


@app.route("/<x1>/<x2>")
def xandy(x1, x2):
    return render_template(
        "index.html",
        x=int(int(x1) / 2),
        y=int(int(x2) / 2),
        color1="red",
        color2="black",
    )


@app.route("/<x1>/<x2>/<c1>/<c2>")
def advanced(x1, x2, c1, c2):
    return render_template(
        "index.html", x=int(int(x1) / 2), y=int(int(x2) / 2), color1=c1, color2=c2
    )


if __name__ == "__main__":
    app.run(debug=True)
