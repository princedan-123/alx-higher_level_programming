#!/usr/bin/python3
"""A script that uses sqlalchemy ORM to list all cities in database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:\
            {port}/{database}"
            )
    Session_class = sessionmaker(bind=engine)
    with Session_class() as session:
        result = session.query(State, City).\
                join(City, City.id == State.id).order_by(City.id).all()
        for state, city in result:
            print(f"{state.name}: ({city.id}) {city.name}")
