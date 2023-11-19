#!/usr/bin/python3
"""Prints the State object with the name as argument from the database"""
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
    new_st = State(name='Louisiana')
    session.add(new_st)
    new_inst = session.query(State).filter_by(name='Louisiana').first()
    print(new_inst.id)
    session.commit()
