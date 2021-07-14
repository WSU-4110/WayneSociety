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
import uuid
from flask import Flask
from flask_login import LoginManager 

app = Flask(__name__)
db = SQLAlchemy()



# Working Model
app.secret_key = 'secretkeylol'

    # This is to configue and setup database
app.config['SECRET_KEY'] = 'HHIIDUNUXUU&&DHKJI' #Temporary
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)
   
Set_Login = LoginManager()
Set_Login.login_view = 'app.Login'
Set_Login.init_app(app)



@Set_Login.user_loader
def Loader_User(Get_User_id):
    return User.query.get(int(Get_User_id))



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

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
    return redirect(url_for('Home'))


# app for Users to signup to use platform
@app.route('/Signup')
def Signup():
    return render_template('Signup.html')

# We want to create a function that takes all the user information on the website (e.g: password) and encrpyt it and store in the database


@app.route('/Signup', methods=['POST'])
def Get_Sign_Up():

    Get_Email = request.form.get('email')
    Get_Name = request.form.get('name')
    Get_Password = request.form.get('password')

    Website_User = User.query.filter_by(email=Get_Email).first()

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


@app.route('/Jobs')
def Jobs():
    return render_template('Jobs.html')

# app for Attractions


@app.route('/Attractions')
def Attractions():
    return render_template('Attractions.html')


@app.route('/Services')
def Services():
    return render_template('Services.html')

# app for Events


@app.route('/Events')
def Events():
    return render_template('Events.html')


@app.route('/Food')
def Food():
    return render_template('Food.html')


@app.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')


# app for Users to view their profile
# We should also show the users information on this page so they know they are currently logged in


@app.route('/Profile')
def Profile():
    return render_template('Profile.html', name=current_user.name, email=current_user.email)


# app for Users loging out of platform
@app.route('/Logout')
@login_required
def Logout():
    logout_user()
    return redirect(url_for('Welcome'))


@app.route('/ResetPassword')
def resetPassword_request():
    return render_template('ResetPassowrd.html', title='Reset_Password')

    # web: gunicorn app:app

if __name__ == "__main__":
    app.run(debug=True)



