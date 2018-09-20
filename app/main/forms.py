from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required
from profanityfilter import ProfanityFilter


pf = ProfanityFilter()

class PostForm(FlaskForm):
    content = TextAreaField("What's on your mind?",validators=[Required()])
    submit = SubmitField('Post')
    

class CommentForm(FlaskForm):
    description = TextAreaField('Help out',validators=[Required()])
    submit = SubmitField("Reply")
