from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from .config import MONGODB_URL#, MIN_CONNECTIONS_COUNT, MAX_CONNECTIONS_COUNT

class DBClient(object):
	
	def __init__(self):
		self.client = MongoClient('192.168.1.110:20000',
								  username='root',
								  password='Q!W@E#r4t5y6',
								  authSource='admin',
								  )

	def connect_to_mongo(self):
		print(f"Mongo URL: {MONGODB_URL}")
		#self.client = AsyncIOMotorClient(str(MONGODB_URL),maxPoolSize=MAX_CONNECTIONS_COUNT, minPoolSize=MIN_CONNECTIONS_COUNT)
		admin = self.client.admin
		col = admin.test_collection
		print(col)
		dog = {"name":"ludo", "age":1}
		col.insert(dog)
	def close_mongo_connection(self):
		self.client.close()
