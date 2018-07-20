#!/usr/bin/python3
from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    datas = session.query(City.name, City.id, State.name).join(State).all()
    for data in datas:
        print("{}: ({}) {}".format(data[2], data[1], data[0]))
