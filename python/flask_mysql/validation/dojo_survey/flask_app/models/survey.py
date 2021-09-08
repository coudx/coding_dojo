from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Survey:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.loc = data["loc"]
        self.lang = data["lang"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_survey(data):
        is_valid = True
        if len(data["first_name"]) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if len(data["loc"]) < 5:
            flash("City must be at least 5 characters.")
            is_valid = False
        if len(data["comment"]) < 40:
            flash("Comments must be more then 40 characters.")
            is_valid = False
        return is_valid

    @classmethod
    def insert(cls, data):
        query = "insert into survey (first_name, last_name, loc, lang, comment, created_at, updated_at) values ( %(first_name)s, %(last_name)s, %(loc)s, %(lang)s, %(comment)s, now(), now());"
        return connectToMySQL("dojo_survey").query_db(query, data)

    @classmethod
    def get_last_survey(cls):
        query = "select * from survey order by id desc limit 1;"
        return connectToMySQL("dojo_survey").query_db(query)
