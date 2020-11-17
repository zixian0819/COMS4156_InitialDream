
import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db
from flask import Flask
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'yaos12397@gmail.com',
    MAIL_PASSWORD = 'ysw1997617',
))

mail = Mail(app)

bp = Blueprint('reminder', __name__, url_prefix='/reminder')



@bp.route("/reminder")
def send_email():
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    subject='test subject'
    sender=['yaos12397@gmail.com']
    recipients=['cushuwanyao@google.com']
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = 'text_body'
    msg.html = '<h1>HTML body</h1>'
    mail.send(msg)
    return 'sent'

