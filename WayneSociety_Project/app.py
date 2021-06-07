from flask import Blueprint
from . import db

app = Blueprint('app', __name__)



@app.route('/profile')
def profile():
    return 'PlaceHolder'