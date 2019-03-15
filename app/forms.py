from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email


class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('female','Female'), ('male','Male')])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    bio = TextAreaField("Biography", validators=[DataRequired()])
    photo = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Images only!')])
    submit = SubmitField("Add Profile")