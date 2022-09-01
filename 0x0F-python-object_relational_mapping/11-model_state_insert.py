#!/usr/bin/python3
"""
script that prints the first State
object from the database hbtn_0e_6_usa
link : https://stackoverflow.com/questions/3325467/
sqlalchemy-equivalent-to-sql-like-statement
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

    new_name = State(name='Louisiana')
    new_instance_session.add(new_name)
    new_instance_session.new
    new_instance_session.commit()

    print(new_name.id)
