"""SQLAlchemy models fro Twitoff"""
from flask_sqlalchemy import SQLAlchemy 

DB = SQLAlchemy()

class User(DB.Model):
    """Twitte users that we query and store historical tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(15), unique=True, nullable=False)


class Tweets(DB.Model):
    """stores tweets"""
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))