#from motor.motor_asyncio import AsyncIOMotorClient
import json
from pymongo import MongoClient
from ..core.config import MONGO_HOST,MONGO_PORT,MONGO_USER,MONGO_PASS,MONGO_DB,MONGO_AUTH_TYPE


class MongoConnection(object):	
    def __init__(self):
        self.client = None
        self.db = None

    def connect_to_mongo(self):
        #self.client = AsyncIOMotorClient(str(MONGODB_URL),maxPoolSize=MAX_CONNECTIONS_COUNT, minPoolSize=MIN_CONNECTIONS_COUNT)
        self.client = MongoClient(f'{MONGO_HOST}:{MONGO_PORT}',
                                   username=MONGO_USER,
                                   password=MONGO_PASS,
                                   authSource='admin',
                                   authMechanism=MONGO_AUTH_TYPE)
        if not self.client:
            print(f'ERROR: Unable to connect to the mongo db.')
            return False

        self.db = self.client.doggy
        return True

    def insert(self, value, collection):
        try:
            value_obj = json.loads(value)
        except ValueError as e:
            print(f'ERROR: Invalid JSON data sent to insert(). {e}')
            return False
        if collection == 'users':
            self.db.users.insert(value_obj)
            print(f'User {value_obj} inserted!')
        return True

    def find(self, pattern):
        pass

    def close_mongo_connection(self):
        self.client.close()


conn = MongoConnection()
