#!/usr/bin/python3
"""
python file that contains the class definition of a City and an
instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """
    This generates the City table with the following:
    Autogenerate an PK ID
    Name of state
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
