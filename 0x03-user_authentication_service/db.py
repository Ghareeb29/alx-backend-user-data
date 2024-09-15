#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.

        Args:
            email (str): The email of the user.
            hashed_password (str): The hashed password of the user.

        Returns:
            User: The newly created User object.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except InvalidRequestError:
            self._session.rollback()
            raise
        except Exception as e:
            self._session.rollback()
            raise
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user in the database by the given keyword arguments.

        Args:
            **kwargs: The keyword arguments to search for.

        Returns:
            User: The first user that matches the given keyword arguments.

        Raises:
            NoResultFound: If no results are found.
            InvalidRequestError: If invalid query arguments are passed.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
        except InvalidRequestError:
            raise
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes in the database.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs: Arbitrary keyword arguments representing
            user attributes to update.

        Raises:
            ValueError: If an invalid attribute is passed
            or if the user is not found.
        """
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError(f"Invalid attribute: {key}")
            self._session.commit()
        except NoResultFound:
            raise ValueError(f"User with id {user_id} not found")
        except InvalidRequestError:
            self._session.rollback()
            raise ValueError("Invalid update request")
