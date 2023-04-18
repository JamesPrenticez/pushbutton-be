import os
from dotenv import load_dotenv
import urllib
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
	ENV=os.getenv('ENVIROMENT')
	APP_NAME='PushButton'
	BASE_DIR = os.path.abspath(os.curdir)
	JSONIFY_PRETTYPRINT_REGULAR = True # Format JSON output for the api

class Development_Config(Config):
	SECRET_KEY=os.getenv("SECRET_KEY"),

class Testing_Config(Config):
	SECRET_KEY=os.getenv("SECRET_KEY"),

class Production_Config(Config):
	SECRET_KEY=os.getenv("SECRET_KEY"),

config={
	'development': Development_Config,
	'testing': Testing_Config,
	'production': Production_Config,
}