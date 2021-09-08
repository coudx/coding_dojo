from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "select * from author;"
        results = connectToMySQL("books").query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def insert(cls, name):
        query = "insert into author (name, created_at, updated_at) values ( %(name)s, now(), now());"
        data = {"name": name}
        return connectToMySQL("books").query_db(query, data)

    @classmethod
    def get(cls, id):
        query = "select name from author where id = %(id)s;"
        data = {"id": id}
        return connectToMySQL("books").query_db(query, data)

    @classmethod
    def get_rest(cls, id):
        query = "select * from author where id not in (select author.id from author join favorite on author.id=favorite.author_id where favorite.book_id=%(id)s);"
        data = {"id": id}
        results = connectToMySQL("books").query_db(query, data)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
