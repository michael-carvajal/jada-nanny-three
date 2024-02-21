from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Email

class AboutPageForm(FlaskForm):
    first_para = TextAreaField('First Para', validators=[DataRequired()])
    second_para = TextAreaField('Second Para', validators=[DataRequired()])
    