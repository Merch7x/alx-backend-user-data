"""Create a class to handle authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Handles authentication to the APi"""

    def require_auth(self, path: str, excluded_paths:
                     List[str]) -> bool:
        """Define paths that require authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """Sets the authentication header with
          username and passowrd encoded string
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Defines current user"""
        return None
