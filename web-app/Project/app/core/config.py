import os

from dotenv import load_dotenv

load_dotenv('.env')
API_HOSTNAME = os.getenv('API_HOSTNAME')
UNIX_EPOCH_GMT = os.getenv('UNIX_EPOCH_GMT')
