from flask import Blueprint
from flask import render_template
from . import db

app = Blueprint('app', __name__)

#ToDO: Moved to Sprint 2  ->
# Implement Efficient Object Oriented Practices for routing

# @app.route('/')
# def Welcome():
#     return render_template('Welcome.html')

# @app.route('/profile')
# def profile():
#     return render_template('Profile.html' )