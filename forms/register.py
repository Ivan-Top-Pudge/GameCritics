from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, PasswordField, StringField, FileField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    login = StringField('Login*', validators=[DataRequired()])
    password = PasswordField('Пароль')
    password_again = PasswordField('Подтвердите пароль')
    name = StringField('Имя')
    surname = StringField('Фамилия')
    email = EmailField('Email*')
    profile_photo = FileField('Фото профиля')
    submit = SubmitField('Зарегистрироваться')
