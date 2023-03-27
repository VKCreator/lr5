from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError



class GameForm(FlaskForm):
    userGuessNumberInput = IntegerField('userGuessNumber', validators=[InputRequired()],
    render_kw={'placeholder':'Введите число...', 'class': 'form-control'})
    submit = SubmitField("Угадать", render_kw={'class':'btn btn-sm btn-primary', 'formaction':'/game', 'formmethod':'post'})
