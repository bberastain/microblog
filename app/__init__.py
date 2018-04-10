from flask import Flask
from config import Config

app = Flask(__name__) #creates appliation object as instance of class Flask
# set to name of module in which it is used
app.config.from_object(Config)

from app import routes # not the previously defined variable
# this is the app package defined by the app directory and __init__.py script
