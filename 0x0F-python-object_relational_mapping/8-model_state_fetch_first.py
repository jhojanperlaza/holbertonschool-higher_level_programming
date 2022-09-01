#!/usr/bin/python3
"""
script that prints the first State
object from the database hbtn_0e_6_usa
"""
import sys
from xml.etree.ElementTree import Element
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    new_instance_session = Session()

    element = new_instance_session.query(State).order_by(State.id).first()
    if element:
        print("{}: {}".format(element.id, element.name))
    else:
        print("Nothing")
