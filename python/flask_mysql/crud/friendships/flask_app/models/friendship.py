from flask_app.config.mysqlconnection import connectToMySQL


class Friendship:
    def __init__(self, data):
        self.user = data["user"]
        self.friend = data["friend"]

    @classmethod
    def insert(cls, data):
        query = "insert into friendship (user_id, friend_id, created_at, updated_at) values (%(user_id)s, %(friend_id)s, now(), now());"
        return connectToMySQL("friendships").query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "select distinct concat(user_id, friend_id) as idx, concat_ws(' ', user.first_name, user.last_name) as user, concat_ws(' ', friend.first_name, friend.last_name) as friend from friendship join user on user.id = friendship.user_id join user as friend on friend.id = friendship.friend_id where friendship.user_id <> friendship.friend_id;"
        result = connectToMySQL("friendships").query_db(query)
        friends = []
        for obj in result:
            friends.append(cls(obj))
        return friends
