import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-12345'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database', 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AVATAR_STORAGE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'avatars')
