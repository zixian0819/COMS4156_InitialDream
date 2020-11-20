"""Import packages for crawler."""
import re
import requests
from bs4 import BeautifulSoup
from flask import Blueprint, render_template, flash
from flaskr.db import get_db

BP = Blueprint('travel', __name__, url_prefix='/travel')


@BP.route('/update')
def get_info():
    """Get state info."""
    target = 'https://covid19.nj.gov/faqs/nj-information/travel-' \
             'and-transportation/which-states-are-on-the-travel-advisory-' \
             'list-are-there-travel-restrictions-to-or-from-new-jersey'
    req = requests.get(url=target)
    html = req.text
    bfbf = BeautifulSoup(html)
    texts = bfbf.find_all('ul')
    ssss = texts[1].text
    process1 = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", ssss)
    process2 = "".join(process1.split(' ')).split('\n')
    states = list(filter(lambda x: x != '', process2))
    # return states
    database = get_db()
    database.execute('DELETE FROM' + ' ' + 'high_risk_states')
    database.commit()
    save(states)
    flash('update successfully')
    return render_template('update.html')


def save(states):
    """Save data into database."""
    for i, _ in enumerate(states):
        database = get_db()
        database.execute(
            'INSERT INTO high_risk_states (id, statename) VALUES (?, ?)',
            (i, states[i])
        )
        database.commit()
