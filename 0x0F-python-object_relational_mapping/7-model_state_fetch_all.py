#!/usr/bin/python3
"""
    a script that selects all the state in a table
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

arg = sys.argv
username = arg[1]
passwd = arg[2]
database = arg[3]
if len(arg) == 4:
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.
            format(username, passwd, database)
            )
    Session = sessionmaker(bind=engine)
    session_object = Session()
    result = session_object.query(State).all()
    for record in result:
        print(str(record.id) + ': ', record.name)
session_object.close
