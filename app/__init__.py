from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__, template_folder=templates, static_folder=static)


SECRET_KEY = os.environ.get('SECRET_KEY') or "ajajajjsjsjajjajaaw333"
#app configuration
app_settings = os.environ.get(
    'APP_SETTINGS'
    'app.config'
) 
app.config.from_object(app_settings)


#connecting to database
MONGO_URI = os.environ.get('MONGO_URI') or "mongodb+srv://andrew_uche:andrewuche4810@cluster0.fcitc.mongodb.net/HEALTHAPP?retryWrites=true&w=majority"

#initializing PyMongo
mongo = PyMongo(app, MONGO_URI)

from app import views2