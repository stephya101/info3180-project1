from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired,FileField, FileAllowed
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class NewProperty(FlaskForm):
    property_title = StringField("Property Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    no_of_rooms = StringField("No. of Rooms", validators=[DataRequired()])
    no_of_bthrooms = StringField("No. of Bathrooms", validators=[DataRequired()])
    price = StringField("Price", validators=[DataRequired()])
    property_type = SelectField("Property Type", choices= ['House', 'Apartment'], validators=[DataRequired()])
    photo = FileField("Photo", validators=[FileRequired(), FileAllowed(['jpeg', 'jpg', 'png'], 'File types accepted')])
    location = StringField("Location", validators=[DataRequired()])