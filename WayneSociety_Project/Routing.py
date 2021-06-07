# All Routing will be done here

# Import Dependecies for Validation, Authorization and routing
from flask import Blueprint
from flask import render_template, redirect
from flask import url_for, request
from flask import flash
from werkzeug.security import generate_password_hash 
from werkzeug.security import check_password_hash
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required



Routing = Blueprint('Routing', __name__)

# Landing page when server starts running
@Routing.route('/')
def Home():
    return render_template('Home.html')

#Routing for Users to Login to use platform
@Routing.route('/Login')
def Login():
    return render_template('Login.html')


#Routing for Users to signup to use platform
@Routing.route('/Signup')
def Signup():
    return render_template('Signup.html')


# ROuting for Users to view their profile
def Profile():
    return render_template('Profile.html')


# Routing for Users loging out of platform
@Routing.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('Home.index'))




# Todo: Add Other routing for navigation (e.g) Attractions, Service, Food, Welcome, etc
# Todo: Setup Database
# Query Database

