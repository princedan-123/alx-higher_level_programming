#!/usr/bin/python3
"""a script that creates a city table"""
import sys
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from model_state import Base, State

arg = sys.argv
username = arg[1]
passwd = arg[2]
database = arg[3]
if len(arg) == 4:
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".
            format(username, passwd, database)
            )
    class City (Base):
        """
            A class that should map to a table in MYSQL database
            it contains the following attributes which corresponds
            to columns of the table in the data base
            id: integer column with a PRIMARY KEY constraint
            name: string column with a NOT NULL constraint
            state_id: integer column with a NOT NULL and FOREIGN KEY
            constraint
        """
        __tablename__ = "Cities"
        id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey("states.id", name="fk_states.id"), nullable=False)
    Base.metadata.create_all(engine)
