#!/usr/bin/env python3
"""User model for a database table named users"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User class for representing entries in the users table.

    Attributes:
        id (int): The integer primary key.
        email (str): A non-nullable string representing the user's email.
        hashed_password (str): A non-nullable string for the hashed password.
        session_id (str): A nullable string for the session ID.
        reset_token (str): A nullable string for the reset token.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self) -> str:
        """
        Return a string representation of the User instance.

        Returns:
            str: A string representation of the User.
        """
        return f"User(id={self.id}, email={self.email})"
