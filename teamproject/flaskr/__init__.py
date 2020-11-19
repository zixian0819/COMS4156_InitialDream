import os

from flask import Flask, send_from_directory
from flask_login import LoginManager
from flaskr.user import User


def create_app(test_config=None):

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

    # where this function should be？
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import dailypass
    app.register_blueprint(dailypass.bp)

    from . import ocr
    app.register_blueprint(ocr.bp)

    from . import index
    app.register_blueprint(index.bp)

    from . import travel
    app.register_blueprint(travel.bp)

    from . import quarantine
    app.register_blueprint(quarantine.bp)

    @app.route('/')
    def serve():
        return send_from_directory(app.static_folder, 'index.html')
    return app
