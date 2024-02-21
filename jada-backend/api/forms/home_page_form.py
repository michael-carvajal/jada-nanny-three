from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class HomePageForm(FlaskForm):
    site_title = StringField('Site Title', validators=[DataRequired()])
    site_subtitle = StringField('Site Subtitle', validators=[DataRequired()])
    page_text = StringField('Home Page Text')
   