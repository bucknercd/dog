import uuid
import argon2


ph = argon2.PasswordHasher()

def verify_password(plain_password, password_hash, password_salt):
    print(f'plain: {plain_password}')
    print(f'phash: {password_hash}')
    print(f'salt: {password_salt}')
    try:
        ph.verify(password_hash, plain_password + password_salt)
    except Exception as e:
        print(f'Incorrect password {plain_password}. {e}')
        return False

    return True

def generate_password_hash_and_salt(plain_password):
    password_salt = str(uuid.uuid4())
    salted_password_hash = ph.hash(plain_password + password_salt)
    return salted_password_hash, password_salt
