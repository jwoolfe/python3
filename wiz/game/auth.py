import uuid
import hashlib
import binascii
import os.path

DEFAULT_FILENAME = "/srv/users.auth"

def login(name, password):
    user = getuser(name)
    if user is not None:
        salt = user['salt']
        oldhash = user['oldhash']
        if checkpass(password, salt, oldhash):
            return True
    return False

def adduser(name, password):
    user = getuser(name)
    if user is not None:
        salt = getsalt()
        oldhash = hashsalt(password, salt)
        user = {
                'username' : name,
                'salt': salt,
                'oldhash': oldhash,
                }
        users = load()
        users.append(user)
        save(users)
        return True
    return False

def getuser(name):
    users = load()
    for user in users:
        if name == user['username']:
            return user
    return None

def checkpass(password, salt, oldhash):
    newhash = hashsalt(password, salt)
    if oldhash == newhash:
        return True
    return False

def changepass(name, oldpass, newpass):
    if login(name, oldpass):
        # create newusers list
        # get oldusers list
        # for each user in oldusers:
        #   if this user is OUR user, skip it
        #   otherwise add it to newusers
        # save(newusers)
        # adduser(name, newpass)
        return True
    return False

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
                'oldhash': password,
            }
            users.append(user)
    return users

def save(users):
    with open(DEFAULT_FILENAME, 'w') as f:
        for user in users:
            username = user['username']
            salt = user['salt']
            password = user['oldhash']
            line = f'{username}:{salt}:{password}\n'
            f.write(line)