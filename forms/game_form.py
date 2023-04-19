from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    submit = SubmitField('Добавить')
