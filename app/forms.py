from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired

class getGraphs(FlaskForm):
    inputGraph = TextAreaField("Input Graph", validators=[DataRequired()], default="")
    queryGraph = TextAreaField("Query Graph", validators=[DataRequired()], default="")
    submit = SubmitField("Run NemoMapPy")
