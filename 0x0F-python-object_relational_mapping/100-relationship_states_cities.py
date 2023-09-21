#!/usr/bin/python3
""" creates a state and city table with relationship 
"""

from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
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
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    california.cities.append(san_francisco)
    session_object = Session()
    session_object.add(california)
    session_object.add(san_francisco)
    session_object.commit()
