"""get dailypass"""
from flask import (
    Blueprint, flash, render_template, request, jsonify
)
from flaskr.db import get_db

BP = Blueprint('dailypass', __name__, url_prefix='/dailypass')


@BP.route('/submit', methods=['GET', 'POST'])
def submit():
    """submit to get dailypass"""
    if request.method == 'POST':
        currentdb = get_db()

        username = request.form['username']
        date = request.form['date']
        visittime = request.form['visittime']

        symptoms = request.form['symptoms']
        building = request.form["building"]
        user = currentdb.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        state = request.form['state']
        is_highrisk = currentdb.execute('SELECT id FROM high_risk_states '
                                        'WHERE statename = ?',
                                        (state,)).fetchone()

        if user is None:
            error = 'Incorrect username.'
            flash(error)
        if symptoms == '1' or is_highrisk is not None:
            currentdb.execute(
                'INSERT INTO dailypass (username, date,visittime,'
                'building,symptoms) '
                'VALUES (?,?,?,?,?)',
                (username, date, visittime, building, symptoms)
            )
            currentdb.execute('INSERT INTO yellow_pool (yellow_user) VALUES (?)',
                              (username,))
            currentdb.commit()
            return jsonify('yellowpass')
        if symptoms == '0' and is_highrisk is None:
            currentdb.execute(
                'INSERT INTO dailypass '
                '(username, date,visittime,building,symptoms) '
                'VALUES (?,?,?,?,?)',
                (username, date, visittime, building, symptoms)
            )
            currentdb.commit()
            return jsonify('greenpass')

    return render_template('submit.html')
