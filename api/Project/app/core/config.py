import os

from dotenv import load_dotenv
from starlette.datastructures import CommaSeparatedStrings, Secret

API_V1_STR = '/api'

JWT_TOKEN_PREFIX = 'Token'
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week

load_dotenv('.env')

MAX_CONNECTIONS_COUNT = int(os.getenv('MAX_CONNECTIONS_COUNT', 10))
MIN_CONNECTIONS_COUNT = int(os.getenv('MIN_CONNECTIONS_COUNT', 10))
SECRET_KEY = Secret(os.getenv('SECRET_KEY', 'secret key for project'))

#PROJECT_NAME = os.getenv('PROJECT_NAME', 'FastAPI example application')
#ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv('ALLOWED_HOSTS', ''))

MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.getenv('MONGO_PORT', 10000))
MONGO_USER = os.getenv('MONGO_USER', 'root')
MONGO_PASS = os.getenv('MONGO_PASSWORD', 'BOGUS')
MONGO_DB = os.getenv('MONGO_DB', 'doggy')


database_name = MONGO_DB
users_collection_name = 'users'
cookies_collection_name = 'cookies'