#!/usr/bin/python3
"""Prints all the City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    for inst in (session.query(State.name, City.id, City.name)
                 .filter(State.id == City.state_id)):
        print(inst[0] + ": (" + str(inst[1]) + ") " + inst[2])
