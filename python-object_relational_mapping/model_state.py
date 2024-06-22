#!/usr/bin/python3

""" A class that defines a State and an instance Base = declarative_base(). """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
     Defines a state in the database.

    Attributes:
        __tablename__ (str): The name of the MySQL table.
        id (int): The id of the state.
        name (str): The name of the state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
