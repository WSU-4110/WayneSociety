from flask_login import current_user
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

app = Flask(__name__)
db = SQLAlchemy()



# Working Model
app.secret_key = 'secretkeylol'

    # This is to configue and setup database
app.config['SECRET_KEY'] = 'HHIIDUNUXUU&&DHKJI' #Temporary
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)
   
Set_Login = LoginManager()
Set_Login.login_view = 'Login'
Set_Login.init_app(app)


# Loading users
@Set_Login.user_loader
def Loader_User(Get_User_id):
    return User.query.get(int(Get_User_id))


## Creating the database
# Query the database using the model
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
    Return 500 http error
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
def get_Login_Up():

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


# Routing for signup page
@app.route('/Signup')
def Signup():
    return render_template('Signup.html')


# Setting up signup logic
@app.route('/Signup', methods=['POST'])
def Get_Sign_Up():
    """
    We want to create a function that takes all the user information on the website 
    (e.g: password) and encrpyt it and store in the database
    """

    

    Get_Email = request.form.get('email')
    Get_Name = request.form.get('name')
    Get_Password = request.form.get('password')

    Website_User = User.query.filter_by(
        email=Get_Email).first()

    if Website_User:
        """
        # If user is already in in database 
        # re-route back to signup to re-attempt
        """
        # Flag a error message when a user is not logged in
        flash('Email address already exists')
        return redirect(url_for('Signup'))

    # If no user in database, procedd to get all email and password data, also hash password before storing
    Website_New_User = User(email=Get_Email,
                            name=Get_Name,
                            password=generate_password_hash(
                                Get_Password, method='sha256'))

# Storing New user in database, first we query the databse id to see if data already exist, if it doesn't we get the new data and store
    db.session.add(Website_New_User)
    db.session.commit()


# Upon successful sign-up, route to login so users can login using their credentials
    return redirect(url_for('Login'))


# Routing for jobs page
@app.route('/Jobs')
@login_required
def Jobs():
    return render_template('Jobs.html')

# Routing for Attractions
@app.route('/Attractions')
@login_required
def Attractions():
    return render_template('Attractions.html')

# Routing for Services
@app.route('/Services')
@login_required
def Services():
    return render_template('Services.html')

# app for Events
@app.route('/Events')
@login_required
def Events():
    return render_template('Events.html')


#Routing for Food
@app.route('/Food')
@login_required
def Food():
    return render_template('Food.html')


#Routing for AboutUs
@app.route('/AboutUs')
@login_required
def AboutUs():
    return render_template('AboutUs.html')


# Routing for Users to view their profile
# We should also show the users information on this page so they know they are currently logged in
@app.route('/Profile')
@login_required
def Profile():
    return render_template('Profile.html', name=current_user.name, email=current_user.email)


# Routing for Users loging out of platform
@app.route('/Logout')
@login_required
def Logout():
    logout_user()
    return redirect(url_for('Welcome'))


#Routing for Reset Password
@app.route('/ResetPassword')
@login_required
def ResetPassword():
    return render_template('ResetPassword.html', 
    title='Reset_Password')

#Routing for Terms and Conditions
@app.route('/Terms')
@login_required
def Terms():
    return render_template('Terms.html')

#Routing for Privacy Policy
@app.route('/Privacy')
@login_required
def Privacy():
    return render_template('Privacy.html')

if __name__ == "__main__":
    app.run(debug=True)