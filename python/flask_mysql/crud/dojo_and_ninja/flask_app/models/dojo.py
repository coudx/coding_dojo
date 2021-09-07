# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

# model the class after the friend table from our database
class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("dojo_and_ninja").query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add(cls, name):
        query = "insert into dojo (name, created_at, updated_at) values (%(name)s, now(), now() );"
        # data is a dictionary that will be passed into the add method from server.py
        data = {"name": name}
        return connectToMySQL("dojo_and_ninja").query_db(query, data)

    @classmethod
    def get_dojo_with_ninja(cls, id):
        query = "SELECT * FROM dojo join ninja on dojo.id = ninja.dojo_id where dojo.id = %(id_num)s;"
        data = {"id_num": id}
        results = connectToMySQL("dojo_and_ninja").query_db(query, data)
        print(results)
        dojo = cls(results[0])
        dojo.ninjas = []
        for row in results:
            ninja_data = {
                "id": row["ninja.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["ninja.created_at"],
                "updated_at": row["ninja.updated_at"],
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo
