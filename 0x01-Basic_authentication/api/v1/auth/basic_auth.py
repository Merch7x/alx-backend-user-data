#!/usr/bin/env python3
"""Handle authentication to a server
with an encode byte string of
  a password and User
"""
from api.v1.auth.auth import Auth
import base64


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
