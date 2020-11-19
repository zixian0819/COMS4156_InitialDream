from flask_login import UserMixin  # 引入用户基类
from flask_login import LoginManager
from flask import Flask

app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


class User(UserMixin):
    """用户类"""
    def __init__(self, user):
        self.username = user.get("name")
        self.id = user.get("id")
        self.userstatus = user. get("status")

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_userstatus(self):
        return self.userstatus

    def set_userstatus(self, status):
        self.username = status


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
