from pymongo import MongoClient
import os
import certifi

class MongoDB:
    def __init__(self, app=None):
        self.client = None
        self.db = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        uri = app.config.get('MONGO_URI', 'mongodb://localhost:27017/nickgen_db')
        # Use certifi's CA bundle for SSL/TLS verification (fixes Vercel/Serverless handshake issues)
        self.client = MongoClient(uri, tlsCAFile=certifi.where())
        self.db = self.client.get_default_database()

db = MongoDB()
