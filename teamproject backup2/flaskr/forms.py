from flask_wtf import Form

from wtforms import StringField, SubmitField
from wtforms import validators, DataRequired, RadioField, SelectField, TextField


class PassForm(Form):
    name = TextField("username", [validators.Required("Please enter your Username")])


    symptons= SelectField('symptoms', choices=[('0','No'),
                                                ('1','Yes')])
    building = SelectField('building', choices=[('mudd'),
                                                 ('gym')])
    visittime = SelectField('visittime', choices=[('9-12'),
                                                 ('12-17')])
    submit = SubmitField("Send")