from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask, jsonify
)
#from flaskr.db import get_db

from flask import Flask, render_template, request, flash,current_app
from flask_login import current_user, login_required

bp = Blueprint('index', __name__, url_prefix='/index')

@bp.route('/index', methods=('GET', 'POST'))
def index():
    # if not current_user.is_authenticated:
    #     return current_app.login_manager.unauthorized()
    return render_template('index.html')

