"""'defination of the app"""
import os

from flask import Flask, send_from_directory
from flask_login import LoginManager
from flaskr.user import User


def create_app(test_config=None):
    """create the app"""
    app = Flask(__name__, instance_relative_config=True,
                static_folder='client/build', static_url_path='')

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the tests config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.BP)

    from . import dailypass
    app.register_blueprint(dailypass.BP)

    from . import ocr
    app.register_blueprint(ocr.BP)

    from . import index
    app.register_blueprint(index.BP)

    from . import travel
    app.register_blueprint(travel.BP)

    from . import quarantine
    app.register_blueprint(quarantine.BP)
