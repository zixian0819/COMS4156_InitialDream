from bs4 import BeautifulSoup
from flaskr.db import get_db
import requests
import re


def get_info():
    target = 'https://covid19.nj.gov/faqs/nj-information/travel-and-transportation/which-states-are-on-the-travel-advisory-list-are-there-travel-restrictions-to-or-from-new-jersey'
    req = requests.get(url = target) 
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('ul')
    s = texts[1].text
    process1 = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", s)
    process2 = "".join(process1.split(' ')).split('\n')
    states = list(filter(lambda x:x!='',process2))
    return states

def save(states):
    db = get_db()
    db.execute(
        'INSERT INTO high_risk_states (states) VALUES (?)', (states)
    )
    db.commit()
    return None

if __name__ == '__main__':

    states = get_info()
    save(states)
    print('Travel Advisory List Updated!')




