#!/usr/bin/python3

""" A class that defines a State and an instance Base = declarative_base(). """
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

engine = create_engine(f"""mysql://{mysql_username}:{mysql_password}
                       @localhost:3306/{database_name}""")
Base = declarative_base()


class State(Base):
    """
     Defines a state in the database.

    Attributes:
        id (int): The id of the state.
        name (str): The name of the state.
        charset (str): The encodage of the table.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    __table_args__ = {'mysql_charset': 'latin1'}


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
