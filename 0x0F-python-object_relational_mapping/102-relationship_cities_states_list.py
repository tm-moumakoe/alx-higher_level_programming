#!/usr/bin/python3
"""Lists all City objects from the database"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    for inst in session.query(State).order_by(State.id):
        for city_inst in inst.cities:
            print(city_inst.id, city_inst.name, sep=": ", end="")
            print(" -> " + inst.name)
