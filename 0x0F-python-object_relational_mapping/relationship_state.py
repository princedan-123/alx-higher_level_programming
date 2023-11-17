#!/usr/bin/python3
"""A script that uses SQLAlchemy ORM to map a table."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """A class that represents the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", back_populates="state", cascade="all, delete-orphan"
            )
