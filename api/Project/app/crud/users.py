import uuid
from .cookies import is_valid_cookie, create_session_cookie, remove_old_cookies
from ..models.users import UserDB
from ..db.mongodb import conn
from ..core.security import verify_password, generate_password_hash_and_salt
from ..core.config import users_collection

import sys


def create_user(user):
    dbuser = UserDB(**user.dict())
    dbuser.password_hash, dbuser.password_salt = generate_password_hash_and_salt(user.password)
    dbuser.user_id = str(uuid.uuid1())
    _id = conn.db[users_collection].insert(dbuser.dict())
    if _id:
        print("User created.")
        #sys.exit()
        return _id
    else:
        return None
    #print(f'{val}')

def login_user(username, password, session_cookie=None):
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
    print(f'dbuser: {dbuser}')
    remove_old_cookies(dbuser.user_id)

    if session_cookie:
        if is_valid_cookie(session_cookie, dbuser.user_id):
            dbuser = get_user(dbuser.user_id)
            print("LOGGED ON via COOKIE")
    else:
        if verify_password(password, dbuser.password_hash, dbuser.password_salt):
            # valid pass
            session_cookie = create_session_cookie(dbuser.user_id)
            dbuser = get_user(dbuser.user_id)
            print("LOGGED ON via USER/PASS")
        else:
            # invalid pass
            print("INCORRECT PASSWORD")
            dbuser = "BOGUS USER"
    return dbuser, session_cookie

def get_user(user_id=None, username=None):
    user = None
    if user_id:
        row = conn.db[users_collection].find_one({"user_id": user_id})
    elif username:
        row = conn.db[users_collection].find_one({"username": username})
    return UserDB(**row)
    