#!/usr/bin/python3

"""
Write a script that lists all State objects from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported

"""

if __name__ == "__main__":
    from model_state import State, Base
    import sqlalchemy
    from sqlalchemy.orm import declarative_base, sessionmaker
    from sqlalchemy import create_engine, Column, String, Integer
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    my_session = sessionmaker(bind=engine)
    session = my_session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    session.close()
