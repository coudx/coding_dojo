from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.fname = data["first_name"]
        self.lname = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def add(cls, data):
        query = "insert into dojo (first_name, last_name, age, created_at, updated_at) values (%(fname)s, %(lname)s, %(age)s, now(), now() );"
        # data is a dictionary that will be passed into the add method from server.py
        return connectToMySQL("dojo_and_ninja").query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "select * from ninja"
        results = connectToMySQL("dojo_and_ninja").query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
