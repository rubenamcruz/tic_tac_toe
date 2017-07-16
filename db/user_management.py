from db.entities import db, User
from hashlib import sha256


def add_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return False
    user = User(username, hashing(password))
    db.session.add(user)
    db.session.commit()
    return True


def hashing(password):
    hashed_password = sha256(password.encode('utf-8'))
    return hashed_password.hexdigest()


def validate_login(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False, "Username doesn't exist!"
    hashed_password = hashing(password)
    if hashed_password == user.password:
        return True, "Successfully added new user!"
    else:
        return False, "Wrong password!"


def change_user_password(user, password):
    user.change_password(hashing(password))
    db.session.commit()
