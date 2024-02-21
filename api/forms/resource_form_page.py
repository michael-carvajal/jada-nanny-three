from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, DateTimeField, URLField
from wtforms.validators import DataRequired, Email

class ResourcePageForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    url = URLField('URL', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    
    