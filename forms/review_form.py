from flask_wtf import FlaskForm
from wtforms import TextAreaField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class ReviewForm(FlaskForm):
    rate = FloatField('Оценка', validators=[DataRequired(), NumberRange(1, 5)])
    content = TextAreaField('Отзыв', validators=[DataRequired()])
    submit = SubmitField('Оставить отзыв')
