#!/usr/bin/env python3
"""Handle authentication to a server
with an encode byte string of
  a password and User
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Handle basic authentication to the server"""
    pass
