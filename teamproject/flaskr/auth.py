""""auth"""
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

BP = Blueprint('auth', __name__, url_prefix='/auth')


@BP.route('/register', methods=('GET', 'POST'))
def register():
    """register function"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        currentdb = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif currentdb.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            currentdb.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            currentdb.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@BP.route('/login', methods=('GET', 'POST'))
def login():
    """login function"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        currentdb = get_db()
        error = None
        user = currentdb.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index.index'))

        flash(error)

    return render_template('auth/login.html')


@BP.before_app_request
def load_logged_in_user():
    """load log in"""
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@BP.route('/logout')
def logout():
    """log out"""
    session.clear()
    return redirect(url_for('auth.login'))
