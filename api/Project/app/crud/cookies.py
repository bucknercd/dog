# cookies in crud
import time
#import base64
import uuid
import calendar
from ..models.users import UserDB
from ..models.cookies import Cookie, Type
from ..db.mongodb import conn
from ..core.config import cookies_collection, ACCESS_COOKIE_EXPIRE_SECONDS


def get_db_cookies(user_id=None, cookie_type='session'):
    if not user_id:
        return ''
    else:
        rows = conn.db[cookies_collection].find({ "$and": [ {"type": cookie_type}, {"user_id": user_id} ]})
    cookies = []
    for row in rows:
        cookies.append(Cookie(**row))
    return cookies

def create_session_cookie(user_id):
    now = time.gmtime() # seconds since epoch as a struct
    timestamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', now) # UTC timestamp
    value = str(uuid.uuid1())
    session_cookie = Cookie(_type=Type.session, key='LS', value=value, user_id=user_id, create_date=timestamp)
    conn.db[cookies_collection].insert(session_cookie.dict())
    return session_cookie

def is_valid_cookie(session_cookie, user_id):
    if not session_cookie:
        return None
    if not expired(session_cookie):
        return True
    else:
        return False
           
def remove_old_cookies(user_id, cookie_type='session'):
    session_cookies = get_db_cookies(user_id=user_id)
    for session_cookie in session_cookies:
        if expired(session_cookie):
            conn.db[cookies_collection].remove({"value": session_cookie.value})

def expired(session_cookie):
    if session_cookie.create_date:
        pass
    else:
        session_cookie = conn.db[cookies_collection].find({"value": session_cookie.value})
    session_cookie_epoch_secs = utc_string_to_epoch_secs(session_cookie.create_date)
    now = round(time.time())
    if now - session_cookie_epoch_secs > ACCESS_COOKIE_EXPIRE_SECONDS:
        return True
    else:
        return False
    
def utc_string_to_epoch_secs(timestamp):
    utc_time = time.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    epoch_time_secs = calendar.timegm(utc_time)
    return epoch_time_secs

    # compare cookie.create_time