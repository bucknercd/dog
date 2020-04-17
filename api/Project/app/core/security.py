from argon2 import PasswordHasher


ph = PasswordHasher()

def verify_password(plain_password, password_hash):
    try:
        ph.verify(password_hash, plain_password)
    except VerifyMismatchError as e:
        print(f'Incorrect password {plain_password}. {e}')
        return False

    return True

def generate_password_hash(plain_password):
    password_hash = ph.hash(plain_password)
    return password_hash
