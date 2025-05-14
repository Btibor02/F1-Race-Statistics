import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/f1_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    