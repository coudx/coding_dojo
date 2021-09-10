from flask_app.config.mysqlconnection import connectToMySQL

# from mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class User:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.username = data["username"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def insert(cls, data):
        query = "insert into user (first_name, last_name, username, email, password, created_at, updated_at) values ( %(first_name)s, %(last_name)s, %(username)s, %(email)s, %(password)s, now(), now());"
        return connectToMySQL("private_wall").query_db(query, data)

    @staticmethod
    def get(data):
        query = "select username, password from user where username = %(username)s;"
        result = connectToMySQL("private_wall").query_db(query, data)
        print(result)
        return result[0]

    @staticmethod
    def get_userlist(id):
        query = "select id, concat_ws(' ', first_name, last_name) as name from user where id <> %(id)s;"
        data = {"id": id}
        results = connectToMySQL("private_wall").query_db(query, data)
        print(results)
        users = []
        for user in results:
            user_data = {"id": user["id"], "name": user["name"]}
            users.append(user_data)
        return users

    @classmethod
    def getuser(cls, data):
        query = "select * from user where username = %(username)s;"
        result = connectToMySQL("private_wall").query_db(query, data)
        for user in result:
            return user
        return False

    @staticmethod
    def get_name_w_id(id):
        query = "select concat_ws(' ', first_name, last_name) as name from user where id= %(id)s;"
        data = {"id": id}
        result = connectToMySQL("private_wall").query_db(query, data)
        for name in result:
            return name

    @staticmethod
    def get_by_email(data):
        query = "select username, passord from user where username = %(email)s;"
        return connectToMySQL("private_wall").query_db(query, data)

    @staticmethod
    def validUser(data):
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

    @classmethod
    def get_by_id(cls, id):
        query = "select * from user where id = %(id)s;"
        data = {"id": id}
        result = connectToMySQL("private_wall").query_db(query, data)
        for user in result:
            return user
