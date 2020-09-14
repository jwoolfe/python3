import uuid
import hashlib
import binascii
import os.path

DEFAULT_FILENAME = "/srv/users.auth"

def getsalt():
    return uuid.uuid4().hex

def hashsalt(password, salt):
    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    protocol = 'sha512'
    count = 100000
    step1 = hashlib.pbkdf2_hmac(protocol, password, salt, count)
    step2 = binascii.hexlify(step1).decode('utf-8')
    return step2

def load():
    if not os.path.isfile(DEFAULT_FILENAME):
        with open(DEFAULT_FILENAME, 'w') as f:
            f.write("")
    users = []
    with open(DEFAULT_FILENAME, 'r') as f:
        for line in f:
            username, salt, password = line.strip().split(':')
            user = {
                'username' : username,
                'salt': salt,
                'password': password,
            }
            users.append(user)
    return users

def save():
    pass
            
