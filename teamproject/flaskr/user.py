"""Import UserMixin."""
from flask_login import UserMixin
from flask_login import LoginManager
from flask import Flask

APP = Flask(__name__)
LOGIN_MANAGER = LoginManager()
LOGIN_MANAGER.login_view = 'auth.login'
LOGIN_MANAGER.init_app(APP)


class User(UserMixin):
    """用户类"""
    # initialize
    def __init__(self, user):
        """Initialize."""
        self.username = user.get("name")
        self.userid = user.get("id")
        self.userstatus = user.get("status")

    def get_username(self):
        """Get the username."""
        return self.username

    def set_username(self, username):
        """Set the username."""
        self.username = username

    def get_userstatus(self):
        """Get the userstatus"""
        return self.userstatus

    def set_userstatus(self, status):
        """Set the userstatus"""
        self.username = status


@LOGIN_MANAGER.user_loader
def load_user(user_id):
    """Load the user."""
    return User.get_username(user_id)
