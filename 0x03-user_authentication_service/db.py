#!/usr/bin/env python3
""" Create User """
from sqlalchemy import create_engine, tuple_
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import Base, User


Class DB:
    """ DB Class """

    def __init__(self) -> None:
        """ Initialize a new DB instance. """
        self._engine = create_engine("sqlite:///a.db",
