#!/usr/bin/env python3
"""An authentication mechanism"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Create a hashed_password"""
    p_hash = hashpw(password.encode('utf-8'), gensalt())
    return p_hash


def _generate_uuid() -> str:
    """generate uuid"""
    return str(uuid4())


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
            raise ValueError(f"User {user.email} already exists")
        except NoResultFound:
            hashed_passwrd = _hash_password(password)
            res = self._db.add_user(email, hashed_passwrd)
            return res

    def valid_login(self, email: str, password: str) -> bool:
        """Credentials validation"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                if checkpw(password.encode('utf-8'),
                           user.hashed_password) is True:
                    return True
                else:
                    return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Creates a session id"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                user_id = int(user.id)
                self._db.update_user(user_id, session_id=session_id)
            return session_id
        except NoResultFound:
            return

    def get_user_from_session_id(self, session_id: str) -> User:
        """Finds a user by session ID"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys a users session"""
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            return

    def get_reset_password_token(self, email: str) -> str:
        """Generates a reset passowrd token"""
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the users password"""
        if not reset_token or not password:
            raise ValueError

        user = self._db.find_user_by(reset_token=reset_token)
        if not user:
            raise ValueError

        pass_hash = _hash_password(password)
        self._db.update_user(
            user.id, hashed_password=pass_hash, reset_token=None)
