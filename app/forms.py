from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet
from wtforms import SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired

class getGraphs(FlaskForm):
    inputGraph = TextAreaField("Input Graph", validators=[DataRequired()], default="")
    queryGraph = TextAreaField("Query Graph", validators=[DataRequired()], default="")
    submit = SubmitField("Run NemoMapPy")

class getFiles(FlaskForm):
    #ensureText = UploadSet('text', 'txt')
    #FileAllowed(ensureText, u"Text Files Only!")
    getInput = FileField("Input File", validators=[FileRequired()])
    getQuery = FileField("Query File", validators=[FileRequired()])
    submit = SubmitField("Send Files")