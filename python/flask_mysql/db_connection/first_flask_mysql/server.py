from flask import Flask, render_template

# import the class from friend.py
from friend import Friend

# import the class from world.py
from world import Cities

app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    cities = Cities.get_all()

    return cities


if __name__ == "__main__":
    app.run(debug=True)
