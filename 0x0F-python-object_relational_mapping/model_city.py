#!/usr/bin/python3


"""
Module that connects a python script to the database

"""
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()

class City(Base):
    """Defining the city class"""
    __tablename__ = 'cities'

    id = Column(String, primary_key=True, autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'))
