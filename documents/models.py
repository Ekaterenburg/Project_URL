import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Dish(Base):
    '''
    блюдо
    '''
    __tablename__ = 'dish'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)
    origin = sq.Column(sq.String, nullable=True)
    recipe = sq.Column(sq.String, nullable=True)
    dish_category = sq.Column(sq.String, nullable=True)
    complexity = sq.Column(sq.String, nullable=True)
    ingredients = sq.Column(sq.String, nullable=True)

class Origin(Base):
    '''
    происхождение
    '''
    __tablename__ = 'origin'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)

class Recipe(Base):
    '''
    рецепт
    '''
    __tablename__ = 'recipe'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sq.Column(sq.String, nullable=False)
    surname = sq.Column(sq.String, nullable=False)
    nickname = sq.Column(sq.String, nullable=False)

class Dish_category(Base):
    """
    категория
    """
    __tablename__ = 'dish_category'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)
    country = sq.Column(sq.Integer, sq.ForeignKey('country.id'), nullable=True)

class Complexity(Base):
    '''
    сложность
    '''
    __tablename__ = 'complexity'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)

class Ingredients(Base):
    '''
    ингредиенты
    '''
    __tablename__ = 'ingredients'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)
'''
class BookAutor(Base):
    __tablename__ = 'book-autor'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_autor = relationship(Autor, backref='autor_book')
'''
def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)