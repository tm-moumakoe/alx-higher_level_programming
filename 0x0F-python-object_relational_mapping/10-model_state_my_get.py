#!/usr/bin/python3
"""prints the State object with the name passed as argument from the database"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    inst = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(inst[0].id)
    except IndexError:
        print("Not found")
