#!/usr/bin/python3
"""using sqlachemy library to work with database"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
import sys
Base = declarative_base()
arg = sys.argv
username = sys.argv[1]
passwd = sys.argv[2]
database = sys.argv[3]
engine = create_engine(
        """mysql://{}:{}@localhost:3306/{}""".
        format(username, passwd, database)
        )


class State(Base):
    """A class that maps to a states table in the database"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
