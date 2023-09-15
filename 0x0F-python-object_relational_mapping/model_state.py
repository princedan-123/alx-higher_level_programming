#!/usr/bin/python3
"""using sqlachemy library to work with database"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import sys
Base = declarative_base()
arg = sys.argv
username = sys.argv[1]
passwd = sys.argv[2]
database = sys.argv[3]


class State(Base):
    """A class that maps to a states table in the database"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
