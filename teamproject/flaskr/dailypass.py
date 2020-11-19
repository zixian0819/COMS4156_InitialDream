from flask import (
    Blueprint, flash, render_template, request, jsonify
)
from flaskr.db import get_db


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
        state = request.form['state']
        is_highrisk = db.execute('SELECT id FROM high_risk_states '
                                 'WHERE statename = ?',
                                 (state,)).fetchone()

        if user is None:
            error = 'Incorrect username.'
            flash(error)
        if symptoms == '1' or is_highrisk is not None:
            db.execute(
                'INSERT INTO dailypass (username, date,visittime,'
                'building,symptoms) '
                'VALUES (?,?,?,?,?)',
                (username, date, visittime, building, symptoms)
            )
            db.execute('INSERT INTO yellow_pool (yellow_user) VALUES (?)',
                       (username,))
            db.commit()
            return jsonify('yellowpass')
        if symptoms == '0' and is_highrisk is None:
            db.execute(
                'INSERT INTO dailypass '
                '(username, date,visittime,building,symptoms) '
                'VALUES (?,?,?,?,?)',
                (username, date, visittime, building, symptoms)
            )
            db.commit()
            return jsonify('greenpass')

    return render_template('submit.html')
