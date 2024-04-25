#!/usr/bin/env python3
"""4. Hash password"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """
    string arguments and returns bytes.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ should take mandatory email and password
        string arguments and return a User object.

        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError(f'User {email} already exists')
