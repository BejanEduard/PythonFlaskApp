from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,  SubmitField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo, Email


class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField("Email", validators=[DataRequired, Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField("Sign up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")