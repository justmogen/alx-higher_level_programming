#!/usr/bin/python3
# Import modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

# Check if the script is executed and not imported
if __name__ == '__main__':
    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine and a session to connect to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and order them by id
    states = session.query(State).order_by(State.id).all()

    # Print each state's id and name
    for state in states:
        print(f'{state.id}: {state.name}')

    # Close the session
    session.close()
