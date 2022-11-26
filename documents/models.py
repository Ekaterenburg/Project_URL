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
    origin = sq.Column(sq.String, sq.ForeignKey('origin.id'), nullable=True)
    recipe = sq.Column(sq.String, sq.ForeignKey('recipe.id'), nullable=True)
    dish_category = sq.Column(sq.String, sq.ForeignKey('dish_category.id'), nullable=True)
    complexity = sq.Column(sq.Integer, sq.ForeignKey('complexity.id'), nullable=True)
    ingredients = sq.Column(sq.String, sq.ForeignKey('ingredients.id'), nullable=True)

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
    title = sq.Column(sq.String, nullable=False)
    manual = sq.Column(sq.String, nullable=False)

class Dish_category(Base):
    """
    категория
    """
    __tablename__ = 'dish_category'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    title = sq.Column(sq.String, nullable=False)

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
    enabling = sq.Column(sq.Integer, nullable=False)

def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)