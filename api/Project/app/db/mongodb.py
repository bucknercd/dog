#from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from ..core.config import MONGO_HOST,MONGO_PORT,MONGO_USER,MONGO_PASS,MONGO_DB
class DBClient(object):	
    def __init__(self):
        self.client = MongoClient(f'{MONGO_HOST}:{MONGO_PORT}',
				   username=MONGO_USER,
				   password=MONGO_PASS,
				   authSource='admin',
                                   # the auth type 
                                   )

    def connect_to_mongo(self):
        #self.client = AsyncIOMotorClient(str(MONGODB_URL),maxPoolSize=MAX_CONNECTIONS_COUNT, minPoolSize=MIN_CONNECTIONS_COUNT)
        db = self.client.doggy
        user_valeria = {"userid":9999, "name": "Valeria Buckner", "zip_code":76502}
        db.users.insert(user_valeria)
        print(f'User "{user_valeria} inserted!')

    def close_mongo_connection(self):
        self.client.close()
