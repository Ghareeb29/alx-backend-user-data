#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != "/":
            path += "/"
        for ex_path in excluded_paths:
            if ex_path[-1] != "/":
                ex_path += "/"
            if path == ex_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):  # type: ignore
        """current_user"""
        return None

    def session_cookie(self, request=None) -> str:
        """Returns the session ID from a cookie"""
        if request is None:
            return None
        session_id = os.getenv("SESSION_NAME")
        return request.cookies.get(session_id)
