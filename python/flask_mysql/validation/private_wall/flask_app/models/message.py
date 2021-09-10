from flask_app.config.mysqlconnection import connectToMySQL


class Message:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.user_id = data["user_id"]
        self.sender = data["sender"]
        self.created_at = data["created_at"]

    @staticmethod
    def insert(data):
        query = "insert into message (content, user_id, sender, sender_id) values (%(content)s, %(user_id)s, %(sender)s, %(sender_id)s);"
        return connectToMySQL("private_wall").query_db(query, data)

    @classmethod
    def get_message(cls, id):
        query = "select * from message where user_id=%(id)s;"
        data = {"id": id}
        results = connectToMySQL("private_wall").query_db(query, data)
        messages = []
        for message in results:
            messages.append(message)
        print(messages)
        return messages

    @staticmethod
    def delete(id):
        query = "delete from message where id = %(id)s;"
        data = {"id": id}
        return connectToMySQL("private_wall").query_db(query, data)

    @staticmethod
    def get_num_message_sent(id):
        query = "select count(message.id) as ct, sender_id from message where sender_id = %(id)s group by sender_id;"
        data = {"id": id}
        result = connectToMySQL("private_wall").query_db(query, data)
        print(result)
        for key in result:
            return key["ct"]
        return 0

    @staticmethod
    def filter(id):
        query = "select * from message where id=%(id)s;"
        data = {"id": id}
        result = connectToMySQL("private_wall").query_db(query, data)
        if result:
            return result[0]
        return 0
