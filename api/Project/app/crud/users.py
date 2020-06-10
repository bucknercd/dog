import uuid
from .cookies import is_valid_cookie, create_session_cookie, remove_old_cookies
from ..models.users import UserDB, UserResponse
from ..db.mongodb import conn
from ..core.security import verify_password, generate_password_hash_and_salt
from ..core.config import users_collection, cookies_collection

import sys


def create_user(user):
    dbuser = UserDB(**user.dict())
    dbuser.password_hash, dbuser.password_salt = generate_password_hash_and_salt(user.password)
    dbuser.user_id = str(uuid.uuid1())
    _id = conn.db[users_collection].insert(dbuser.dict())
    if _id:
        print("User created.")
        return _id
    else:
        return None

def login_user(username, password, remember_me):
    dbuser = get_user(username=username)
    if not dbuser:
        return (None, None)
    if verify_password(password, dbuser.password_hash, dbuser.password_salt):
        # valid pass
        session_cookie = create_session_cookie(dbuser.user_id)
        print("LOGGED ON via USER/PASS")
        remove_old_cookies(dbuser.user_id)

    else:
        # invalid pass
        print("INCORRECT PASSWORD")
        return (None, None)
    return UserResponse(**dbuser.dict()), session_cookie

def get_user(user_id=None, username=None, session_cookie=None):
    row = None
    if user_id:
        row = conn.db[users_collection].find_one({"user_id": user_id})
    elif username:
        row = conn.db[users_collection].find_one({"username": username})
    elif session_cookie:
        row = conn.db[cookies_collection].find_one({"key": "LS", "value": session_cookie})
        print(f"user id: {row['user_id']}")
        return get_user(user_id=row['user_id'])
    print(f'ROW: {row}')
    if row:
        return UserDB(**row)
    else:
        return None
    