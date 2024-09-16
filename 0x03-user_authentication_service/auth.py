#!/usr/bin/env python3
"""
Authentication module
"""
import uuid
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted hash of the input password.
    """
    # Convert the password string to bytes
    password_bytes = password.encode("utf-8")

    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password


class Auth:
    """Auth class to interact with the authentication database."""

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            User: The newly created User object.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            # Check if user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # If user doesn't exist, create a new one
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate a login attempt.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode("utf-8"),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """
        Generate a UUID.

        Returns:
            str: The generated UUID.
        """
        return str(uuid.uuid4())

    def create_session(self, email: str) -> str:
        """
        Create a session for a user.

        Args:
            email (str): The email of the user.

        Returns:
            str: The session ID.
        """
        user = self._db.find_user_by(email=email)
        session_id = self._generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Get a user from a session ID.

        Args:
            session_id (str): The session ID to get the user from.

        Returns:
            User: The user object associated with the session ID.
        """
        if session_id is None:
            return None
        else:
            user = self._db.find_user_by(session_id=session_id)
            return user

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy a session for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            None
        """
        self._db.update_user(user_id, session_id=None)
        return None

    def __init__(self):
        self._db = DB()
