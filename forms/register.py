from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, PasswordField, StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class RegisterForm(FlaskForm):
    login = StringField('Login*', validators=[DataRequired("Обязательное поле")])
    password = PasswordField('Пароль*', validators=[DataRequired("Обязательное поле")])
    password_again = PasswordField('Подтвердите пароль*', validators=[DataRequired("Обязательное поле")])
    name = StringField('Имя')
    surname = StringField('Фамилия')
    email = EmailField('Email*')
    profile_photo = FileField('Фото профиля', validators=[FileAllowed(['jpg', 'png'], 'Только jpg и png!')])
    submit = SubmitField('Зарегистрироваться')
