from flask_app.config.mysqlconnection import connectToMySQL


class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.page = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "select * from book;"
        results = connectToMySQL("books").query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def insert(cls, data):
        query = "insert into book (title, num_of_pages, created_at, updated_at) values ( %(title)s, %(page)s, now(), now())"
        return connectToMySQL("books").query_db(query, data)

    @classmethod
    def get(cls, id):
        query = "select title from book where id = %(id)s;"
        data = {"id": id}
        return connectToMySQL("books").query_db(query, data)

    @classmethod
    def get_rest(cls, id):
        query = "select * from book where id not in (select book.id from book left join favorite on book.id=favorite.book_id where favorite.author_id = %(id)s);"
        data = {"id": id}
        results = connectToMySQL("books").query_db(query, data)
        books = []
        for book in results:
            books.append(cls(book))
        return books
