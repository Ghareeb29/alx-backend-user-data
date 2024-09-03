#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple


class BasicAuth(Auth):
    """Basic Auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header
        for a Basic Authentication.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes a Base64-encoded authorization header.

        Args:
            base64_authorization_header (str):
            The Base64-encoded authorization header.

        Returns:
            str: The decoded authorization header,
            or None if the input is invalid.
        """

        if base64_authorization_header is None or not isinstance(
            base64_authorization_header, str
        ):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """
        Extracts user credentials from a decoded Base64 authorization header.

        Args:
            decoded_base64_authorization_header (str):
            The decoded Base64 authorization header.

        Returns:
            tuple: A tuple containing the email and password,
            or (None, None) if the input is invalid.
        """
        if decoded_base64_authorization_header is None or not isinstance(
            decoded_base64_authorization_header, str
        ):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password
