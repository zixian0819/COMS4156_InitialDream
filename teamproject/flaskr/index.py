from flask import Blueprint, render_template
# from flask_login import current_user, login_required

bp = Blueprint('index', __name__, url_prefix='/index')


@bp.route('/index', methods=('GET', 'POST'))
def index():
    # if not current_user.is_authenticated:
    #     return current_app.login_manager.unauthorized()
    return render_template('index.html')
