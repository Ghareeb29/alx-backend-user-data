#!/usr/bin/env python3
"""
This module provides a function for hashing passwords securely.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password: A string representing the password to be hashed.

    Returns:
        A byte string representing the salted, hashed password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
