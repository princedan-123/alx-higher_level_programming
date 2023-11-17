#!/usr/bin/python3
"""A script that uses relationship on state objects."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:\
            {port}/{database}"
            )
    Base.metadata.create_all(engine)
    Session_class = sessionmaker(bind=engine)
    with Session_class() as session:
        New_state = State(
                name="California", cities=[City(name="San Francisco")]
                )
        session.add(New_state)
        session.commit()
