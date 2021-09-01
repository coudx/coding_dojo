from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"first_name": "Michael", "last_name": "Choi"},
    {"first_name": "John", "last_name": "Supsupin"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]

print(users[0].keys())


@app.route("/")
def index(dict=users):
    return render_template("index.html", keys=users[0].keys(), dicts=dict)


if __name__ == "__main__":
    app.run(debug=True)
