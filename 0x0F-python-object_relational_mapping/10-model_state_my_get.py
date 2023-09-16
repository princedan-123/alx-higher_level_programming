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
    search = arg[4]
    if len(arg) == 5:
        engine = create_engine(
                "mysql+mysqldb://{}:{}@localhost:3306/{}".
                format(username, passwd, database)
                )
    Session = sessionmaker(bind=engine)
    with Session() as session_object:
        result = session_object.query(State)
        result = result.filter(State.name.like("%{}%".format(search)))
        result = result.first()
        if result is None:
            print("Not found")
        else:
            print(result.id)
