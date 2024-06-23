#!/usr/bin/python3

""" A script that adds the State object "Louisiana"
    to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:"
        f"{mysql_password}@localhost:3306/"
        f"{database_name}")

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(f"{new_state.id}")

    session.close()
