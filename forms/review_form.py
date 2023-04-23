from flask_wtf import FlaskForm
from wtforms import TextAreaField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class ReviewForm(FlaskForm):
    rate = FloatField('Оценка', validators=[DataRequired('Поставьте оценку'), NumberRange(1, 5)])
    content = TextAreaField('Отзыв', validators=[DataRequired('Напишите отзыв')])
    submit = SubmitField('Оставить отзыв')
