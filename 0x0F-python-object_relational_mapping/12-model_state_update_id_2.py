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

    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update is not None:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
