
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask import Flask, request, render_template, redirect, session, url_for



# Import Db SQLite + SQLAlchemy
db = SQLAlchemy()


def create_app():
    
    app = Flask(__name__)
    app.secret_key = 'secretkeylol'


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




    return app