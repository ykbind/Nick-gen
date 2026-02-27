from pymongo import MongoClient
import os

class MongoDB:
    def __init__(self, app=None):
        self.client = None
        self.db = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        uri = app.config.get('MONGO_URI', 'mongodb://localhost:27017/nickgen_db')
        self.client = MongoClient(uri)
        self.db = self.client.get_default_database()

db = MongoDB()
