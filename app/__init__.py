from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) #creates appliation object as instance of class Flask
# set to name of module in which it is used
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models # not the previously defined variable
# this is the app package defined by the app directory and __init__.py script
