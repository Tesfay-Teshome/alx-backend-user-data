#!/usr/bin/env python3
""" User Model """

from sqlalchemy import Colmun, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Colmun(Integer, primary_key=True)
    email = Colmun(String(250), nullable=False)
    hashed_password = Colmun(String(250), nullable=False)
    session_id = Colmun(String(250))
    reset_token = Colmun(String(250))
