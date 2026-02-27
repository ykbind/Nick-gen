import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-12345'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb+srv://ykblmaoind_db_user:yash149@cluster0.qhrlb2h.mongodb.net/nickgen_db?retryWrites=true&w=majority&appName=Cluster0'
    AVATAR_STORAGE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'avatars')
