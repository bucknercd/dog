#from motor.motor_asyncio import AsyncIOMotorClient
import json
import pymongo
from ..core.config import MONGO_HOST,MONGO_PORT,MONGO_USER,MONGO_PASS,MONGO_DB,MONGO_AUTH_TYPE,users_collection


class MongoConnection(object):	
    def __init__(self):
        self.client = None
        self.db = None

    def connect_to_mongo_and_init(self):
        #self.client = AsyncIOMotorClient(str(MONGODB_URL),maxPoolSize=MAX_CONNECTIONS_COUNT, minPoolSize=MIN_CONNECTIONS_COUNT)
        self.client = pymongo.MongoClient(f'{MONGO_HOST}:{MONGO_PORT}',
                                          username=MONGO_USER,
                                          password=MONGO_PASS,
                                          authSource='admin',
                                          authMechanism=MONGO_AUTH_TYPE)
        if not self.client:
            print(f'ERROR: Unable to connect to the mongo db.')
            return False

        self.db = self.client[MONGO_DB]
        self.db[users_collection].create_index('username', unique=True)
        return True

    def close_mongo_connection(self):
        self.client.close()

conn = MongoConnection()
