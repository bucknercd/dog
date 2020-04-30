from bson.objectid import ObjectId
from ..models.users import UserDB
from ..db.mongodb import conn
from ..core.security import verify_password, generate_password_hash_and_salt


def create_user(user):
    dbuser = UserDB(**user.dict())
    dbuser.password_hash, dbuser.password_salt = generate_password_hash_and_salt(user.password)
    _id = conn.insert(dbuser.dict(), 'users')
    return _id
    #print(f'{val}')

def login_user(username, password):
    pass
    # check request header for a session cookie
    # check for cookie and verify that it is valid
    # case one: no cookie
    # verify creds that are supplied are correct
    # create a valid cookie with expiry and store it in DB
    # send back a valid session cookie with the home page: status logged in
    # case two: a valid cookie
    # send back session cookie with the home page: status logged in
    

def get_user(_id=None, username=None):
    user = None
    if _id:
        _id = ObjectId(_id)
        user = conn.find({"_id": ObjectId(_id)})
    elif username:
        user = conn.find({"username": username})

    if user:
        return user
    return None
