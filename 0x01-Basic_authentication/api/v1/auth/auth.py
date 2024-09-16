#!/usr/bin/env python3
"""Create a class to handle authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Handles authentication to the APi"""

    def require_auth(self, path: str, excluded_paths:
                     List[str]) -> bool:
        """Define paths that require authentication"""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        n_path = path.rstrip('/')

        n_e_p = [p.rstrip('/') for p in excluded_paths]
        if n_path not in n_e_p:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """Sets the authentication header with
          username and password encoded string
        """
        if request is None or request.headers.get("Authorization") is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Defines current user"""
        return None
