#!/usr/bin/python3

""" A class that defines a city and inherits from Base. """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
     Defines a city in the database.

    Attributes:
        __tablename__ (str): The name of the MySQL table.
        id (int): The id of the city.
        name (str): The name of the city.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
