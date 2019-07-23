from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import TEXT
from wtforms import SubmitField, TextAreaField, validators
from wtforms.validators import ValidationError, DataRequired

class getGraphs(FlaskForm):
    inputGraph = TextAreaField("Input Graph", validators=[DataRequired()], default="")
    queryGraph = TextAreaField("Query Graph", validators=[DataRequired()], default="")
    submit = SubmitField("Run NemoMapPy")

class getFiles(FlaskForm):
    getInput = FileField("Input File", validators=[FileRequired(), FileAllowed(TEXT, "Must be Text Files")])
    getQuery = FileField("Query File", validators=[FileRequired(), FileAllowed(TEXT, "Must be Text Files")])
    submit = SubmitField("Send Files")