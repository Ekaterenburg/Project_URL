import sqlalchemy as sq
import os
from sqlalchemy.orm import sessionmaker
from models import *

def add_genre(session, list_genre: tuple) -> bool:
    try:
        for genre in list_genre:
            add_ = Genre(title=genre)
            session.add(add_)
        session.commit()
        return True
    except:
        return False

def add_country(session, list_country: tuple) -> bool:
    try:
        for country  in list_country:
            add_ = Country(title=country)
            session.add(add_)
        session.commit()
        return True
    except:
        return False

base_name = 'baza'
DSN = f'sqlite:///{base_name}'
engine = sq.create_engine(DSN)
create_table(engine)

Session = sessionmaker(bind=engine)
session = Session()

list_country = ('Россия', 'Германия', 'Франция', 'США', 'Япония')
list_genre = ('ужасы', "триллер", "комедия", "драмма", "фантастика", "фентези", "документальные", "мемуары", "детектив", "боевик")
add_genre(session, list_genre)
add_country(session, list_country)
session.close()