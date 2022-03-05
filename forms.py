from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[Email(), DataRequired()])
    password = PasswordField(label='password', validators=[Length(min=8), DataRequired()])
    btn_login = SubmitField(label='Log In')
