#!/usr/bin/env python3
"""Create a class to handle authentication"""
from flask import request
from typing import List, TypeVar
import re
from os import getenv


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

        patterns = []
        for p in excluded_paths:
            escaped_path = re.escape(p.rstrip('/'))
            regex_pattern = escaped_path.replace(r'\*', '.*')
            regex_pattern = f"^{regex_pattern}/?$"
            patterns.append(re.compile(regex_pattern))

        for pattern in patterns:
            if pattern.match(n_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Retrives the authentication header
        """
        if request is None or request.headers.get("Authorization") is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Defines current user"""
        return None

    def session_cookie(self, request=None):
        """Return a cookie value from a request"""
        if request is None:
            return None
        cookie = request.cookies.get(getenv("SESSION_NAME"))
        return cookie
