# from mysqlconnection import connectToMySQL
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

database = "recipes"


class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.des = data["des"]
        self.ins = data["ins"]
        self.is_thirty = data["is_thirty"]
        self.created_at = data["created_at"]
        self.user_id = data["user_id"]

    @classmethod
    def get_all_by_uid(cls, id):
        query = "select * from recipe where user_id=%(id)s;"
        data = {"id": id}
        results = connectToMySQL(database).query_db(query, data)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_detail(cls, id):
        query = "select * from recipe where id= %(id)s;"
        data = {"id": id}
        return connectToMySQL(database).query_db(query, data)[0]

    @classmethod
    def update(cls, data):
        query = "update recipe set name=%(name)s, desc=%(des)s, ins=%(ins)s, is_thirty=%(is_thirty)s, self.created_at = %(created_at)s whrere id= %(id)s;"
        return connectToMySQL(database).query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = "delete from recipe where id = %(id)s;"
        data = {"id": id}
        return connectToMySQL(database).query_db(query, data)

    @classmethod
    def add(cls, data):
        query = "insert into recipe (name, des, ins, is_thirty, user_id, created_at) values (%(name)s,%(des)s, %(ins)s, %(is_thirty)s, %(user_id)s, %(created_at)s);"
        return connectToMySQL(database).query_db(query, data)

    @staticmethod
    def validUser(data):
        query = "select user_id from recipe where id = %(id)s;"
        result = connectToMySQL(database).query_db(query, data)
        if result:
            return data["user_id"] == result[0]["user_id"]
        return False

    @staticmethod
    def valid(data):
        is_valid = True
        if len(data["name"]) < 1:
            flash("Name is required", "name")
            is_valid = False
        if len(data["des"]) < 20:
            flash("description of 20 character required", "des")
            is_valid = False
        if len(data["ins"]) < 45:
            flash("Instruction requires at least 45 characters", "ins")
            is_valid = False
        return is_valid

    @staticmethod
    def parseData(id, data):
        parsed = {
            "name": data["name"],
            "des": data["des"],
            "ins": data["ins"],
            "is_thirty": int(data["is_thirty"]),
            "created_at": data["created_at"],
            "user_id": id,
        }
        print("parsed_data: **********************", parsed)
        return parsed
