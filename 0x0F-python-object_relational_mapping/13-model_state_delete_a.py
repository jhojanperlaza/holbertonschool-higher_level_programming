#!/usr/bin/python3
"""
script that deletes all State objects with
a name containing the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    new_instance_session = Session()

    for state in new_instance_session.query(State):
        if 'a' in state.name:
            new_instance_session.delete(state)
    new_instance_session.commit()
