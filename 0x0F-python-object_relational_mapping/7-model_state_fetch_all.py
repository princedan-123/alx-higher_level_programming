#!/usr/bin/python3
"""
    a script that selects all the state in a table
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc
from model_state import Base, State

arg = sys.argv
username = arg[1]
passwd = arg[2]
database = arg[3]
if __name__ == '__main__':
    if len(arg) == 4:
        engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'.
                format(username, passwd, database)
                )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session_object = Session()
        result = session_object.query(State).order_by(asc(State.id)).all()
        for record in result:
            print('{}: {}'.format(record.id, record.name))
        session_object.close
