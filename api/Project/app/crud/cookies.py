# cookies in crud
from ..models.users import UserDB
from ..db.mongodb import conn
from ..core.security import cookies_collection


def get_db_cookie(cookie_type='session', user_id=None):
    if not user_id:
        return ''
    else:
        return conn.db['cookies'].find({ "$and": [ {"type": cookie_type}, {"user_id": user_id} ]})

def create_session_cookie():
    pass

def is_valid_cookie(cookie, user_id):
    if not cookie:
        return None
    db_cookie = get_db_cookie(user_id)
    if not expired(db_cookie):
        pass

def expired():
    pass # here!
    # compare cookie.create_time