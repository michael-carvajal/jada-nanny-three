from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Email

class TestimonialForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    