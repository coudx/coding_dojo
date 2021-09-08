from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def insert(cls, data):
        query = "insert into user (first_name, last_name, created_at, updated_at) values ( %(first_name)s, %(last_name)s, now(), now() );"
        return connectToMySQL("friendships").query_db(query, data)

    @classmethod
    def get_all_user_fullname(cls):
        query = "select * from user;"
        result = connectToMySQL("friendships").query_db(query)
        users = []
        for obj in result:
            users.append(cls(obj))
        return users
