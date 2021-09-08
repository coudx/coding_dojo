from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class Email:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_email(data):
        is_valid = True
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid Email Address!")
            is_valid = False
        return is_valid

    @classmethod
    def insert(cls, email):
        query = "insert into email (email, created_at, updated_at) values ( %(email)s, now(), now());"
        data = {"email": email}
        return connectToMySQL("email").query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "select * from email;"
        result = connectToMySQL("email").query_db(query)
        emails = []
        for email in result:
            emails.append(cls(email))
        return emails

    @classmethod
    def get_last(cls):
        query = "select * from email order by id desc limit 1;"
        return connectToMySQL("email").query_db(query)
