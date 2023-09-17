#!/usr/bin/python3
"""Here goes the code"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{database}')
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    first_state = session.query(State).order_by(State.id).first()

    if first_state is not None:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print('Nothing')

    session.close()
