# Import forms dependences
from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField
from wtforms.validators import DataRequired


# Define SMA / MMS form
class SMAForm(FlaskForm):
    base = IntegerField('base', validators=[DataRequired("Type the base of evaluation/Digite a base de avaliação")])
    period = IntegerField('period', validators=[DataRequired("Type the period /Digite o periodo")])
    demand = DecimalField('demand', validators=[DataRequired("Type the demand /Digite a demanda para este periodo")])

