#!/usr/bin/env python3
"""Module of session auth"""

from api.v1.auth.auth import Auth
import uuid
import os
from typing import TypeVar
from models.user import User


class SessionAuth(Auth):
    """Session Auth class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a new session and returns the session ID.

        Args:
            user_id (str): The ID of the user
            to create a session for. Defaults to None.

        Returns:
            str: The ID of the created session,
            or None if user_id is None or not a string.
        """
        if user_id is None:
            return None
        elif type(user_id) is not str:
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns the user ID associated with the session ID.

        Args:
            session_id (str): The ID of the session.
            Defaults to None.

        Returns:
            str: The ID of the user associated with the session,
            or None if session_id is None or not a string.
        """
        if session_id is None:
            return None
        elif type(session_id) is not str:
            return None
        else:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar("User"):  # type: ignore
        """Returns a User instance based on a cookie value"""
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        """Deletes the user session / logout"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
