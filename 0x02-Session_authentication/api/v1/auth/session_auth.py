#!/usr/bin/env python3
"""Module of session auth"""

from api.v1.auth.auth import Auth
import uuid


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
