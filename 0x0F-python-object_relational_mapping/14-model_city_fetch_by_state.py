#!/usr/bin/python3
""" a script that joins two tables, 
    the tables are state and city tables 
""" 
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

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
    with Session() as session_object:
        result = session_object.query(State, City).filter(State.id == City.state_id)
        result = result.order_by(City.id).all()
        for state, city in result:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
