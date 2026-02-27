from pymongo import MongoClient
import os
import certifi

class MongoDB:
    def __init__(self, app=None):
        self.client = None
        self._db = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        uri = app.config.get('MONGO_URI', 'mongodb://localhost:27017/nickgen_db')
        # Use certifi's CA bundle for SSL/TLS verification (fixes Vercel/Serverless handshake issues)
        # Added connectTimeoutMS and connect=False for better serverless performance
        self.client = MongoClient(
            uri, 
            tlsCAFile=certifi.where(),
            connectTimeoutMS=30000,
            socketTimeoutMS=None,
            connect=False
        )
        # Lazy initialization via property
        self._db = None

    @property
    def db(self):
        if self._db is None:
            self._db = self.client.get_default_database()
        return self._db

db = MongoDB()
