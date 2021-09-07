# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

# model the class after the friend table from our database
class Users:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.email = data["email"]
        self.created_at = data["created_at"]

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT id, concat_ws(' ', first_name, last_name) as name, email, created_at FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("users").query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add(cls, data):
        query = "insert into users (first_name, last_name, email, created_at, updated_at) values (%(fname)s, %(lname)s, %(email)s, now(), now() );"
        # data is a dictionary that will be passed into the add method from server.py
        return connectToMySQL("users").query_db(query, data)
