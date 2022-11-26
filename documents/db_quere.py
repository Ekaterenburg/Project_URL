import sqlalchemy as sq
import os
from sqlalchemy.orm import sessionmaker
from models import *
'''
def add_genre(session, list_genre: tuple) -> bool:
    try:
        for genre in list_genre:
            add_ = Genre(title=genre)
            session.add(add_)
        session.commit()
        return True
    except:
        return False
'''
def add_origin(session, list_origin: tuple) -> bool:
    try:
        for origin in list_origin:
            add_ = Origin(title=origin)
            session.add(add_)
        session.commit()
        return True
    except:
        return False

base_name = 'kulinar-book'
DSN = f'sqlite:///{base_name}'
engine = sq.create_engine(DSN)
create_table(engine)

Session = sessionmaker(bind=engine)
session = Session()

list_origin = ('Вьетнам ', 'Китай ', 'Тайланд', 'Южная Корея', 'Япония')
add_origin(session, list_origin)
session.close()