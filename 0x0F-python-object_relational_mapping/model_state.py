#!/usr/bin/python3
"""using sqlachemy library to work with database"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
        A class State that is mapped to a states table in the database
        it has the following columns:
        id: it would contain integer values with with constraints
        name: it would contain string values with constraints
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
