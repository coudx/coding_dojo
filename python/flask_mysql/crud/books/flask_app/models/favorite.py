from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.authors import Author
from flask_app.models.books import Book


class Fav:
    def __init__(self, data):
        self.bood_id = data["book_id"]
        self.author_id = data["author_id"]

    @classmethod
    def get_book_fav_by_author(cls, id):
        query = "select * from favorite join book on book.id=favorite.book_id where favorite.author_id = %(id)s;"
        data = {"id": id}
        results = connectToMySQL("books").query_db(query, data)
        object = []
        for data in results:
            sub_data = {
                "id": data["book.id"],
                "title": data["title"],
                "num_of_pages": data["num_of_pages"],
                "created_at": data["book.created_at"],
                "updated_at": data["book.updated_at"],
            }
            object.append(Book(sub_data))
        return object

    @classmethod
    def get_author_fav_the_book(cls, id):
        query = "select * from favorite join author on author.id=favorite.author_id where favorite.book_id = %(id)s;"
        data = {"id": id}
        results = connectToMySQL("books").query_db(query, data)
        object = []
        for data in results:
            sub_data = {
                "id": data["author.id"],
                "name": data["name"],
                "created_at": data["author.created_at"],
                "updated_at": data["author.updated_at"],
            }
            object.append(Author(sub_data))
        return object

    @classmethod
    def insert(cls, id):
        query = (
            "insert into favorite (book_id, author_id) values (%(books)s, %(authors)s);"
        )
        return connectToMySQL("books").query_db(query, id)
