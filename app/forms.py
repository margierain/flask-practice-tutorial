from flask.ext.wtf import Form 
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid =StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('save_password', default=False)