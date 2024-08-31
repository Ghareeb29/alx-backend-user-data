#!/usr/bin/env python3
"""
This module provides functions for hashing and validating passwords securely.
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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate whether the provided password matches the hashed password.

    Args:
        hashed_password: A byte string representing the hashed password.
        password: A string representing the password to validate.

    Returns:
        A boolean indicating whether the password is valid.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
