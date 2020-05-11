from .mongodb import conn

def connect_to_mongo():
    conn.connect_to_mongo_and_init()

def close_mongo_connection():
    conn.close_mongo_connection()

