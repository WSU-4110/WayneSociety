from flask_login import current_user
from flask import Blueprint
from flask import render_template, redirect
from flask import url_for, request
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import UserMixin
from flask import Flask
from flask_login import LoginManager 
from functools import wraps
from flask import current_app
from flask_recaptcha import ReCaptcha
import os
from werkzeug.wrappers import response
import requests, json


app = Flask(__name__)
db = SQLAlchemy()



# Working Model
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# get reCapthat keys from environment variables
app.config["RECAPTCHA_PUBLIC_KEY"] = os.environ.get('RECAPTCHA_PUBLIC_KEY')
app.config["RECAPTCHA_PRIVATE_KEY"] = os.environ.get('RECAPTCHA_PRIVATE_KEY')
recaptcha = ReCaptcha(app=app)




# DB Initalization
db.init_app(app)
   
Set_Login = LoginManager()
Set_Login.login_view = 'app.Login'
Set_Login.init_app(app)


# Loading users
@Set_Login.user_loader
def Loader_User(Get_User_id):
    return User.query.get(int(Get_User_id))


# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))



# Handling page not found errors
@app.errorhandler(404)
def page_not_found(e):

    """
    Return a custom 404 error.
    """
    return render_template('404.html'), 404


#Handling server errors
@app.errorhandler(500)
def server_error(e):

    """
    Return 503 http error
    """
    app.logger.error(f"Server error: {e}, route: {request.url}")
    return render_template('500.html'), 500

# Handing authentication errors
@app.errorhandler(403)
def not_authenticated(e):
    """
    Return 403 http error
    """
    app.logger.error(f"Server error: {e}, route: {request.url}")
    return render_template('403.html'), 403




# Landing page when server starts running
@app.route('/')
def Welcome():
    return render_template('Welcome.html')


@app.route('/Home')
def Home():
    return render_template('Home.html')

# app for Users to Login to use platform
@app.route('/Login')
def Login():
    return render_template('Login.html')


@app.route('/Login', methods=['POST'])
def Get_Login_Up():

    Get_Email = request.form.get('email')
    Get_Password = request.form.get('password')
    Set_Remember = True if request.form.get('remember') else False
    

    Website_User = User.query.filter_by(email=Get_Email).first()

    # Validate Password, and check if the user data is in database
    if not Website_User or not check_password_hash(Website_User.password, Get_Password):
        flash('Check login information')
        return redirect(url_for('Login'))

    login_user(Website_User, remember=Set_Remember)
    return redirect(url_for('Jobs'))


# app for Users to signup to use platform
@app.route('/Signup')
def Signup():
    return render_template('Signup.html')

# We want to create a function that takes all the user information on the website (e.g: password) and encrpyt it and store in the database




@app.route('/Signup', methods=['POST'])
def Get_Sign_Up():

    sitekey = "6Lcqp64bAAAAAO-aJ2Dd99bwYqK__B6FVods6gTB"


    Get_Email = request.form.get('email')
    Get_Name = request.form.get('name')
    Get_Password = request.form.get('password')
    captcha_resonse = request.form.get('g-recaptcha-response')
    

    Website_User = User.query.filter_by(email=Get_Email).first()


    if request.method == 'POST':
        captcha_resonse = request.form.get('g-recaptcha-response')

        if Validate_Recaptcha(captcha_resonse, sitekey) == True:
            if not Website_User:
                new_user = User(email=Get_Email, name=Get_Name, password=Get_Password)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect(url_for('Jobs'))
            else:
                flash('This email has already been used')
                return redirect(url_for('Signup'))
    
    # If user is already in in database re-route back to signup to re-attempt
    if Website_User:
        # Flag a error message when a user is not logged in
        flash('Email address already exists')
        return redirect(url_for('Signup'))

    # If no user in database, procedd to get all email and password data, also hash password before storing
    Website_New_User = User(email=Get_Email, name=Get_Name,
                            password=generate_password_hash(Get_Password, method='sha256'))

# Storing New user in database, first we query the databse id to see if data already exist, if it doesn't we get the new data and store
    db.session.add(Website_New_User)
    db.session.commit()


# Upon successful sign-up, route to login so users can login using their credentials
    return redirect(url_for('Login'))




def Validate_Recaptcha(captcha_response):
    """ 
    Validating recaptcha response from google server
    Returns True captcha test passed for submitted form else returns False.
    """

    secret = "6Lcqp64bAAAAALDL3Ctg3JrodEk-ct02-0NolRYc"
    payload = {'response': captcha_response, 'secret': secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = response.json()
    return response_text['success']



# Routing for Jobs
@app.route('/Jobs')
def Jobs():
    return render_template('Jobs.html')


# Routing for Attractions
@app.route('/Attractions')
def Attractions():
    return render_template('Attractions.html')


# Routing for Services
@app.route('/Services')
def Services():
    return render_template('Services.html')

# Routing for Events
@app.route('/Events')
def Events():
    return render_template('Events.html')

# Routing for Food
@app.route('/Food')
def Food():
    return render_template('Food.html')

# Routing for AbousUs
@app.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')


# Routing for Users to view their profile
# We should also show the users information on this page so they know they are currently logged in
@app.route('/Profile')
def Profile():
    return render_template('Profile.html', name=current_user.name, email=current_user.email)



# Routing for Users loging out of platform
@app.route('/Logout')
def Logout():
    logout_user()
    return redirect(url_for('Welcome'))


# Routing for users to reset their password
@app.route('/ResetPassword')
def ResetPassword():
    return render_template('ResetPassword.html', title='Reset_Password')



if __name__ == "__main__":
    app.run(debug=True)



