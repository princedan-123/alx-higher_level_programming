#!/usr/bin/python3
"""a script that selects all the state in a table"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

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
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session_object = Session()
        first_state = session_object.query(State).order_by(State.id).first()
        if first_state is None:
            print("Nothing")
        else:
            print("{}: {}".format(first_state.id, first_state.name))
        session_object.close()
