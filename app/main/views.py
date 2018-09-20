from . import main
from flask import render_template
from flask_login import login_required, current_user
from ..models import User, Crisis, Commentcrisis, Fam, Commentfam, Health, Commenthealth, Mental, Commentmental
from .forms import PostForm, CommentForm


@main.route('/')
def home():
    """
    Function that renders the home page
    """
    title="Welcome | Safe Space"

    return render_template('home.html', title=title)


@main.route('/about')
def about():
    """
    Function that renders the about page
    """
    title="About Us"

    return render_template('about.html')


@main.route('/index')
def index():
    """
    Function that returns the index which has all the categories
    """

    return render_template('index.html')


@main.route('/identity')
def identity():
    """
    Function that chooses the identity crisis category
    """
    identities=Crisis.query.all()
    if identities is None:
        abort(404)
    form = PostForm()
    if form.validate_on_submit():
        content = form.content.data
        new_crisis=Crisis(content=content,user_name=current_user.username)
        new_crisis.save_crisis

    return render_template('crisis.html',form=form,identities=identities)


@main.route('/fam')
def fam():
    """
    Function that chooses the family issues category
    """

    return render_template('fam.html')


@main.route('/mental')
def depression():
    """
    Function that chooses the depression category
    """

    return render_template('mental.html')


@main.route('/health')
def health():
    """
    Function that chooses the family issues category
    """

    return render_template('health.html')




    
