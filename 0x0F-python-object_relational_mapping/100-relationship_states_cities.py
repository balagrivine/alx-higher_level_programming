#!/usr/bin/python3


"""
Write a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost at port 3306
You must use the cities relationship for all State objects
Your code should not be executed when imported
"""

if __name__ == "__main__":
    #import slqalchemy
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from sys import argv
    from relationship_city import City, Base
    from relationship_state import State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    #new_state = State(name='California')
    #new_city = City(name='San Francisco')

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()

    session.close()
