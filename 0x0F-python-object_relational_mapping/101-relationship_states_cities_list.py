#!/usr/bin/python3
"""
    A script that prints states objects and their corresponding cities

"""

from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    arg = sys.argv
    username = arg[1]
    passwd = arg[2]
    database = arg[3]
    if len(arg) == 4:
        engine = create_engine(
                "mysql+mysqldb://{}:{}@localhost:3306/{}".
                format(username, passwd, database)
                )
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State, City).order_by(State.id, City.id).all()
    for state_obj in result:
        print("{}: {}".format(state_obj[0].id, state_obj[0].name))
        for city in state_obj[0].cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close
