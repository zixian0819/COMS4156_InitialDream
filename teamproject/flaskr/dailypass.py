import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask, jsonify
)
from flaskr.db import get_db

from flask import Flask, render_template, request, flash
# import forms


bp = Blueprint('dailypass', __name__, url_prefix='/dailypass')

@bp.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        db = get_db()

        username = request.form['username']
        date = request.form['date']
        visittime = request.form['visittime']

        symptoms = request.form['symptoms']
        building = request.form["building"]
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        error=None
        print(symptoms)
        if user is None:
            error = 'Incorrect username.'
        if symptoms == '1':
            db.execute(
                'INSERT INTO dailypass (username, date,visittime,building,symptoms) VALUES (?,?,?,?,?)',
                (username, date, visittime, building, symptoms)
            )
            db.commit()
            return render_template('yellowpass.html')
        if error is None:
            db.execute(
                'INSERT INTO dailypass (username, date,visittime,building,symptoms) VALUES (?,?,?,?,?)',
                (username, date, visittime, building, symptoms)
            )
            db.commit()
            return render_template('greenpass.html')
        flash(error)
    return render_template('submit.html')
