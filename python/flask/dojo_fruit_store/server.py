from flask import Flask, render_template, request, redirect
import os

imgPath = os.path.join("static", "img")

app = Flask(__name__)
app.config["img_folder"] = imgPath


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/checkout", methods=["POST"])
def checkout():
    num = (
        int(request.form["apple"])
        + int(request.form["raspberry"])
        + int(request.form["blackberry"])
        + int(request.form["strawberry"])
    )
    return render_template("checkout.html", items=num, data=request.form)


@app.route("/fruits")
def fruits():
    apple = os.path.join(app.config["img_folder"], "apple.png")
    blackberry = os.path.join(app.config["img_folder"], "blackberry.png")
    raspberry = os.path.join(app.config["img_folder"], "raspberry.png")
    strawberry = os.path.join(app.config["img_folder"], "strawberry.png")
    return render_template(
        "fruits.html", a=apple, b=blackberry, r=raspberry, s=strawberry
    )


if __name__ == "__main__":
    app.run(debug=True)
