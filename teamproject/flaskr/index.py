from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask, jsonify
)
from flaskr.db import get_db

from flask import Flask, render_template, request, flash
from flask_login import current_user, login_required

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/index', methods=('GET', 'POST'))
@login_required
def index():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     db = get_db()
    #
    #
    #     if not username:
    #         error = 'Username is required.'
    #     elif not password:
    #         error = 'Password is required.'
    #     elif db.execute(
    #         'SELECT id FROM user WHERE username = ?', (username,)
    #     ).fetchone() is not None:
    #         error = 'User {} is already registered.'.format(username)
    #
    #     if error is None:
    #         db.execute(
    #             'INSERT INTO user (username, password) VALUES (?, ?)',
    #             (username, generate_password_hash(password))
    #         )
    #         db.commit()
    #         return redirect(url_for('auth.login'))
    #
    #     flash(error)

    return render_template('index.html',username=current_user)