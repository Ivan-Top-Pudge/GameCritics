from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired


class GameForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    logo = FileField('Логотип', validators=[FileAllowed(['jpg', 'png'], "Только jpg и png"), FileRequired()])
    description = TextAreaField('Описание')
    developer = StringField('Разработчик/Издатель', validators=[DataRequired("Укажите разработчика/издателя")])
    submit = SubmitField('Добавить')
