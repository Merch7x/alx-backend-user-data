#!/usr/bin/env python3
"""Implement password hashing"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password"""
    bp = password.encode('utf-8')
    hashed = bcrypt.hashpw(bp, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check the validity of a password"""
    byte_pas = password.encode('utf-8')
    if bcrypt.checkpw(byte_pas, hashed_password):
        return True

    return False
