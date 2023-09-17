#!/usr/bin/python3
"""a script that joins two tables"""
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
        result = session_object.query(State.name, City.id, City.name)
        result = result.join(City, State.id == City.state_id)
        result = result.order_by(City.id).all()
        for row in result:
            state_name = row[0]
            city_id = row[1]
            city_name = row[2]
            print("{}: ({}) {}".format(state_name, city_id, city_name))

