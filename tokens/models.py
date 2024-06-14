from pymongo import MongoClient


def get_db():
    client = MongoClient("mongodb+srv://admin:myhomePassword@cluster0.m5kp7d2.mongodb.net/")
    db = client['new_db']
    return db

class MongoUser:
    def __init__(self, user_data):
        self._id = user_data['_id']
        self.username = user_data['username']
        self.password = user_data['password']
        

    def __str__(self):
        return self.username