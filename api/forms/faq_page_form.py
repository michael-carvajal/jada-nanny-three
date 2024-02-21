from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Email

class FAQPageForm(FlaskForm):
    question = TextAreaField('Question', validators=[DataRequired()])
    answer = TextAreaField('Answer', validators=[DataRequired()])
    
    