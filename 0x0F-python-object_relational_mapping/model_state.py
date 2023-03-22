#!/usr/bin/python3

# Import SQLAlchemy modules
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative base
Base = declarative_base()

# Define the State class that inherits from Base
class State(Base):
    # Link to the MySQL table states
    __tablename__ = 'states'
    # Define the id column with auto-generated, unique integer, primary key and not null
    id = Column(Integer, primary_key=True, nullable=False)
    # Define the name column with string of maximum 128 characters and not null
    name = Column(String(128), nullable=False)
