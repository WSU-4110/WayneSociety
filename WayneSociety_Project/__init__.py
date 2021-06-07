# __INIT__ to configue ap

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import Db SQLite + SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    

   
    from .Routing import Routing as Routing_blueprint
    app.register_blueprint(Routing_blueprint)



    from .app import app as app_blueprint
    app.register_blueprint(app_blueprint)

    return app