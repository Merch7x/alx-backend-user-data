#!/usr/bin/env python3
"""Handle authentication to a server
with an encode byte string of
  a password and User
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """Handle basic authentication to the server"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns a base64 parth of the auth header"""
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        h_list = authorization_header.split(" ")

        if h_list[0] != "Basic" and h_list[-1] != " ":
            return None

        return h_list[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decode value of a Base64 header"""
        if base64_authorization_header is None or\
                not isinstance(base64_authorization_header, str):
            return None

        try:
            value = base64.b64decode(
                base64_authorization_header)
            return value.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str)\
            -> Tuple[str, str]:
        """returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None\
                or not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        h_list = decoded_base64_authorization_header.split(':')
        if len(h_list) != 2:
            return (None, None)
        email, passwd = h_list
        return (email, passwd)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password."""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        if not User.all() or User.count == 0:
            return None

        try:
            users = User.search({"email": user_email})
            if not users:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
                return None
        except Exception:
            return None
