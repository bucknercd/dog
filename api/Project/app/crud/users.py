from bson.objectid import ObjectId
from .cookies import is_valid_cookie, create_session_cookie
from ..models.users import UserDB
from ..db.mongodb import conn
from ..core.security import verify_password, generate_password_hash_and_salt
from ..core.security import users_collection


def create_user(user):
    dbuser = UserDB(**user.dict())
    dbuser.password_hash, dbuser.password_salt = generate_password_hash_and_salt(user.password)
    _id = conn.db[users_collection].insert(dbuser.dict())
    return _id
    #print(f'{val}')

def login_user(username, password, session_cookie=None):
    pass
    # check request header for a session cookie
    # check for cookie and verify that it is valid
    # case one: no cookie
    # verify creds that are supplied are correct
    # create a valid cookie with expiry and store it in DB
    # send back a valid session cookie with the home page: status logged in
    # case two: a valid cookie
    # send back session cookie with the home page: status logged in
    dbuser = get_user(username=username)
    if not dbuser:
        return
    valid_cookie = is_valid_cookie(session_cookie, dbuser._id.__str__())
    if session_cookie:
        if valid_cookie:
            pass # log on
    else:
        if verify_password(password, dbuser.password_hash, dbuser.password_salt):
            # valid pass
            create_session_cookie(dbuser._id.__str__())
            pass
        else:
            # invalid pass
            pass

def get_user(user_id=None, username=None):
    user = None
    if user_id:
        user = conn.db[users_collection].find({"_id": ObjectId(user_id)})
    elif username:
        user = conn.db[users_collection].find({"username": username})
    return user
    