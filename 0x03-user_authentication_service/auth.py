#!/usr/bin/env python3
"""An authentication mechanism"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Create a hashed_password"""
    p_hash = hashpw(password.encode('utf-8'), gensalt())
    return p_hash


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialise Objects"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {user.email} already exists")
        except NoResultFound:
            hashed_passwrd = _hash_password(password)
            res = self._db.add_user(email, hashed_passwrd)
            return res
