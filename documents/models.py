import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Genre(Base):
    '''
    жанры
    '''
    __tablename__ = 'genre'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)

class Autor(Base):
    '''
    авторы
    '''
    __tablename__ = 'autor'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sq.Column(sq.String, nullable=False)
    surname = sq.Column(sq.String, nullable=False)
    nickname = sq.Column(sq.String, nullable=False)

class Book(Base):
    '''
    книги
    '''
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)
    date = sq.Column(sq.Integer, nullable=True)
    rating = sq.Column(sq.String, nullable=True)
    pages = sq.Column(sq.Integer, nullable=True)
    id_genre = sq.Column(sq.Integer, sq.ForeignKey('genre.id'), nullable=False)
    publishinghouse = sq.Column(sq.Integer, sq.ForeignKey('publishinghouse.id'), nullable=True)

class PublishingHouse(Base):
    """
    издательство
    """
    __tablename__ = 'publishinghouse'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)
    country = sq.Column(sq.Integer, sq.ForeignKey('country.id'), nullable=True)

class Country(Base):
    '''
    страны
    '''
    __tablename__ = 'country'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)

class BookAutor(Base):
    __tablename__ = 'book-autor'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_autor = relationship(Autor, backref='autor_book')

def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)