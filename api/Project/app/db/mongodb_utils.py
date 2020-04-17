from .mongodb import conn


def connect_to_mongo():
    conn.connect_to_mongo()

def close_mongo_connection():
    conn.close_mongo_connection()
