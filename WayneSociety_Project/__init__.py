

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, session, url_for
from twilio.rest import Client


# Import Db SQLite + SQLAlchemy
db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = 'secretkeylol'

    # This is to configue and setup database
    app.config['SECRET_KEY'] = 'HHIIDUNUXUU&&DHKJI' #Temporary
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)
   
    Set_Login = LoginManager()
    Set_Login.login_view = 'Routing.Login'
    Set_Login.init_app(app)

    from .models import User

    @Set_Login.user_loader
    def Loader_User(Get_User_id):
        return User.query.get(int(Get_User_id))


    from .Routing import Routing as Routing_blueprint
    app.register_blueprint(Routing_blueprint)

    
    from .app import app as app_blueprint
    app.register_blueprint(app_blueprint)


## Twilio API Email Integration configuration
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN= os.environ.get('TWILIO_AUTH_TOKEN')
    TWILIO_VERIFY_SERVICE = os.environ.get('TWILIO_VERIFY_SERVICE')
    SENDGRID_API_KEY= os.environ.get('SENDGRID_API_KEY') 

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


    return app