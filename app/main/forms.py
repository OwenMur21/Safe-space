from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required



class PostForm(FlaskForm):
    content = TextAreaField("What's pip install flask-migrateon your mind?",validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    description = TextAreaField('Help out',validators=[Required()])
    submit = SubmitField("Comment")
class MessageForm(FlaskForm):
    content = TextAreaField('Message', validators=[Required()])
    submit = SubmitField('Submit')