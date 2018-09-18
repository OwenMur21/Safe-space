from . import main
from flask import render_template

@main.route('/index')
def index():
   """
   Function that returns the index which has all the categories
   """

   return render_template('index.html')
