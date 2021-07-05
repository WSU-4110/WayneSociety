# Using Abstract Factory Design Patterns

from abc import abstractclassmethod, abstractmethod

from flask.templating import render_template_string
from flask_login import current_user
from flask import Blueprint
from flask import render_template, redirect
from flask import url_for, request
from flask import flash
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from .models import User
from .import db
import uuid
import random




Routing = Blueprint('Routing', __name__)


class Website_Routing:
    def __init__(self, Website=None):

        self.Website = Website

    def show_Website(self):


        website_router = self.Website()

        print("Wayne Society")



class Welcome_Routing:

    @Routing.route('/')
    def Welcome():
        return render_template('Welcome.html')

    def __str__(self):
        return render_template_string("Routing for Welcome Page")

class Home_Routing:

    @Routing.route('/Home')
    def Home():
        return render_template('Home.html')

    def __str__(self):
        return render_template_string("Routing for Home Page")

class Login_Routing:

    @Routing.route('/Login')
    def Login():
        return render_template('Login.html')


    @Routing.route('/Login', methods=['POST'])
    def Get_Login_Up():

        Get_Email = request.form.get('email')
        Get_Password = request.form.get('password')
        Set_Remember = True if request.form.get('remember') else False

        Website_User = User.query.filter_by(email=Get_Email).first()

        # Validate Password, and check if the user data is in database
        if not Website_User or not check_password_hash(Website_User.password, Get_Password):
            flash('Check login information')
            return redirect(url_for('Routing.Login'))

        login_user(Website_User, remember=Set_Remember)
        return redirect(url_for('Routing.Home'))


    def __str__(self):
        return render_template_string("Routing for Login Page")



class Signup_Routing:

    @Routing.route('/Signup')
    def Signup():
        return render_template('Signup.html')

    @Routing.route('/Signup', methods=['POST'])
    def Get_Sign_Up():

        Get_Email = request.form.get('email')
        Get_Name = request.form.get('name')
        Get_Password = request.form.get('password')

        Website_User = User.query.filter_by(email=Get_Email).first()

    # If user is already in in database re-route back to signup to re-attempt
        if Website_User:
            # Flag a error message when a user is not logged in
            flash('Email address already exists')
            return redirect(url_for('Routing.Signup'))

    # If no user in database, procedd to get all email and password data, also hash password before storing
        Website_New_User = User(email=Get_Email, name=Get_Name,
                            password=generate_password_hash(Get_Password, method='sha256'))

# Storing New user in database, first we query the databse id to see if data already exist, if it doesn't we get the new data and store
        db.session.add(Website_New_User)
        db.session.commit()


# Upon successful sign-up, route to login so users can login using their credentials
        return redirect(url_for('Routing.Login'))

    def __str__(self):
        return render_template_string("Routing for Signup")


class Website_Categories_Routing:

    @Routing.route('/Jobs')
    def Jobs():
        return render_template('Jobs.html')

    # ROuting for Attractions
    @Routing.route('/Attractions')
    def Attractions():
        return render_template('Attractions.html')


    @Routing.route('/Services')
    def Services():
        return render_template('Services.html')

    # Routing for Events


    @Routing.route('/Events')
    def Events():
        return render_template('Events.html')


    @Routing.route('/Food')
    def Food():
        return render_template('Food.html')


    @Routing.route('/AboutUs')
    def AboutUs():
        return render_template('AboutUs.html')


    # ROuting for Users to view their profile
    # We should also show the users information on this page so they know they are currently logged in


    @Routing.route('/Profile')
    def Profile():
        return render_template('Profile.html', name=current_user.name, email=current_user.email)


    def __str__(self):
        return render_template_string("Routing for categories navigation")



class Logout_Routing:

    # Routing for Users loging out of platform
    @Routing.route('/Logout')
    @login_required
    def Logout():
        logout_user()
        return redirect(url_for('Routing.Welcome'))

    def __str__(self):
        return render_template_string("Routing for Logout")


def random_page():
    return random.choice([Welcome_Routing, Logout_Routing, Website_Categories_Routing, Signup_Routing ])


if __name__=="__main__":
    Website = Website_Routing(random_page)
    for num in range(6):
        Website.show_Website()
