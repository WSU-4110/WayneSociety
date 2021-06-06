# App Code
from enum import unique
from flask import Flask
from flask import render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


app =Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATEBASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'BVHNININNDNINIDN&*H*Y*BDJBUHNDININ'


# Database Setup
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True) # max of 20
    password = db.Column(db.String(80), nullable=False) # Max of 80 Once hashed


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "password"})

    submit = SubmitField("Register")

    def validate_username(self, username):
        Validate_user = User.query.filter_by(
            username=username.data).first()
        if Validate_user:
            raise Validate_user(
                "Already Existing"
            )

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "password"})

    submit = SubmitField("Login")


# Routing
@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/Login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    return render_template('Login.html', form=form)

@app.route('/Signup', methods=['GET', 'POST'])
def SignUp():
    form = RegisterForm()
    return render_template('Signup.html', form=form)

@app.route('/Profile')
def Profile():
    return render_template('Profile.html')



if __name__=='__main__':
    app.run(debug=True)

