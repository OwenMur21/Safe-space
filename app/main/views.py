from . import main
from flask import render_template
from flask_login import login_required, current_user



@main.route('/')
def home():
    """
    Function that renders the home page
    """
    title="Welcome | Safe Space"

    return render_template('home.html', title=title)


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
    # form = PostForm()
    # if form.validate_on_submit():
    #     content = form.content.data


    return render_template('crisis.html')


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




    
