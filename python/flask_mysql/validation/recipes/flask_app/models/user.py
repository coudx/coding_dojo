from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask_app import app

# from mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
bcrypt = Bcrypt(app)
database = "recipes"


class User:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.username = data["username"]
        self.email = data["email"]
        self.created_at = data["created_at"]

    @classmethod
    def insert(cls, data):
        query = "insert into user (first_name, last_name, username, email, password) values ( %(first_name)s, %(last_name)s, %(username)s, %(email)s, %(password)s);"
        return connectToMySQL(database).query_db(query, User.parseData(data))

    @staticmethod
    def get(data):
        query = "select id, password from user where username = %(username)s;"
        return connectToMySQL(database).query_db(query, data)

    @staticmethod
    def get_by_email(data):
        query = "select id from user where email = %(email)s;"
        return connectToMySQL(database).query_db(query, data)

    @classmethod
    def get_by_id(cls, id):
        query = "select * from user where id = %(id)s;"
        data = {"id": id}
        result = connectToMySQL(database).query_db(query, data)
        for user in result:
            return user

    @staticmethod
    def regValid(data):
        user = User.get(data)
        email = User.get_by_email(data)
        is_valid = True
        if len(data["first_name"]) < 2:
            flash("First name requires at least 2 characters.", "first_name")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("Last name requires at least 2 characters.", "last_name")
            is_valid = False
        if len(data["username"]) < 5:
            flash("Username requires at least 5 characters.", "username")
            is_valid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid Email Address!", "email")
            is_valid = False
        if len(data["password"]) < 8:
            flash("Password requires at least 8 characters.", "password")
            is_valid = False
        if data["password"] != data["vpassword"]:
            flash("Password confirm not the same as password", "vpassword")
            is_valid = False
        if user:
            flash("username has been taken", "username")
            is_valid = False
        if email:
            flash("Email has been taken", "username")
            is_valid = False
        return is_valid

    @staticmethod
    def loginValid(data):
        user = User.get(data)[0]
        if not user:
            flash("Invalid Username/Password Combination", "login")
            return False
        print(user, data)
        if not bcrypt.check_password_hash(user["password"], data["password"]):
            flash("Invalid Username/Password Combination", "login")
            return False
        return user["id"]

    @staticmethod
    def parseData(data):
        pw = bcrypt.generate_password_hash(data["password"])
        parsed = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "username": data["username"],
            "email": data["email"],
            "password": pw,
        }
        return parsed
