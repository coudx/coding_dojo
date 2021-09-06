# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

# model the class after the friend table from our database
class Cities:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.country_code = data["country_code"]
        self.district = data["district"]
        self.population = data["population"]
        self.country_id = data["country_id"]

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cities;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("world").query_db(query)
        # Create an empty list to append our instances of friends
        cities = []
        # Iterate over the db results and create instances of friends with cls.
        for city in results:
            cities.append(cls(city))
        return cities
