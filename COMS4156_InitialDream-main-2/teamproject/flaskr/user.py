from flask import Flask
from flask_login import LoginManager, UserMixin

class user(UserMixin):

    def __init__(self, user):
        self.username = user.get('name')
        self.id = user.get('id')