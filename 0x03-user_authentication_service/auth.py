#!/usr/bin/env python3
"""An authentication mechanism"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """Create a hashed_password"""
    p_hash = hashpw(password.encode('utf-8'), gensalt())
    return p_hash
