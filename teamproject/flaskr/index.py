"""index"""
from flask import Blueprint, render_template
# from flask_login import current_user, login_required

BP = Blueprint('index', __name__, url_prefix='/index')


@BP.route('/index', methods=('GET', 'POST'))
def index():
    """index"""
    # if not current_user.is_authenticated:
    #     return current_app.login_manager.unauthorized()
    return render_template('index.html')
