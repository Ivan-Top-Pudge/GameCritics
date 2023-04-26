from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired("Введите логин")])
    password = PasswordField('Пароль', validators=[DataRequired("Введите пароль")])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
