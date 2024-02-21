from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Email

class ContactPageForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    