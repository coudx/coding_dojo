from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class User:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.username = data["username"]
        self.password = data["password"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def insert(cls, data):
        query = "insert into user (first_name, last_name, username, email, password, created_at, updated_at) values ( %(first_name)s, %(last_name)s, %(username)s, %(email)s, %(password)s, now(), now());"
        return connectToMySQL("user").query_db(query, data)

    @classmethod
    def get(cls, data):
        query = "select * from user where username = %(username)s;"
        return connectToMySQL("user").query_db(query, data)

    @staticmethod
    def validUser(data):
        is_valid = True
        if len(data["first_name"]) < 2:
            flash("First name requires at least 2 characters.", "reg")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("Last name requires at least 2 characters.", "reg")
            is_valid = False
        if len(data["username"]) < 5:
            flash("Username requires at least 5 characters.", "reg")
            is_valid = False
        if len(data["password"]) < 8:
            flash("Password requires at least 8 characters.", "reg")
            is_valid = False
        if data["password"] != data["vpassword"]:
            flash("Password confirm not the same as password", "reg")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_id(cls, id):
        query = "select * from user where id = %(id)s;"
        data = {"id": id}
        return connectToMySQL("user").query_db(query, data)
