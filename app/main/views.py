from . import main
from flask import render_template



@main.route('/')
def home():
    """
    Functiom  that renders the home page
    """
    title="Welcome | Safe Space"

    return render_template('home.html', title=title)

    
