#!/usr/bin/python3
""" a script that creates a city table
"""
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

    class City(Base):
        """
            A class that inherits from state class, it has the following
            attributes
            id: it has a not null and primary key constraint, it represents
                the city id which is unique
            name: represents the name of the city. It has not null constraint
            state_id: this column is a foreign key to state.id of the states
                table
        """
        __tablename__ = "cities"
        id = Column(
                Integer, autoincrement=True,
                nullable=False, primary_key=True
                )
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
