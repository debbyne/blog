from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class NewBlogForm(FlaskForm):
    title = StringField('title', validators = [DataRequired()])
    content = TextAreaField("", render_kw={"placeholder": "Type your story..."})
    submit = SubmitField('Submit')