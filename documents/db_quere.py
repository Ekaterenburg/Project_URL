import sqlalchemy as sq
import os
from sqlalchemy.orm import sessionmaker
from models import *

def add_recipe(session, list_recipe: tuple) -> bool:
    try:
        for recipe in list_recipe:
            add_ = Recipe(title=recipe)
            session.add(add_)
        session.commit()
        return True
    except:
        return False

def add_dish(session, list_dish: tuple) -> bool:
    try:
        for dish in list_dish:
            add_ = Dish(title=dish)
            session.add(add_)
        session.commit()
        return True
    except:
        return False

def add_dish_category(session, list_dish_category: tuple) -> bool:
    try:
        for dish_category in list_dish_category:
            add_ = Dish_category(title=dish_category)
            session.add(add_)
        session.commit()
        return True
    except:
        return False

def add_complexity(session, list_complexity: tuple) -> bool:
    try:
        for complexity in list_complexity:
            add_ = Complexity(title=complexity)
            session.add(add_)
        session.commit()
        return True
    except:
        return False

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
list_complexity = ('Лёгкая', "Средняя", "Сложная")
list_dish_category = ('Супы', "Напиткки", "Десерты", "Основное")
list_dish = ('Салат с рисовой лапшой и курицей', 'Куриные ножки в кокосовом чили-соусе', 'Блинчики Бань Сео',
             'Традиционный вьетнамский суп Фо', 'Вьетнамский суп с морепродуктами', 'Куриный суп с тофу и зеленью',
             'Ароматный отварной рис с яйцом', 'Лапша Хоккиен с имбирем с зеленым луком', 'Жареная говядина с имбирем и тофу',
             'Ланчжоуская лапша в говяжьем бульоне', 'Пестрый суп с яичным тофу и креветками', 'Суп из говядины и грибов еноки',
             'Рисовая лапша по-тайски', 'Жареный рис с лапшой и мясом', 'Жареный рис с ананасом и курицей',
             'Манго-кокосовое желе', 'Цукаты из арахиса', 'Кокосовый десерт',
             'Рис с креветками в бульоне', 'Тайский суп Том Кха с кокосовым молоком и курицей', 'Тайский хотпот с морепродуктами',
             'Садко-острая курица с перцем чили', 'Куриная грудка с кунжутным соусом и огурцом', 'Чапче из конжаковой лапши с курицей',
             'Сладкие рисовые пирожные с фасолевой начинкой', 'Печенье в форме рыбки с начинкой и сладкой бобовой пасты', 'Чизкейк из сладкого картофеля и печенья Oreo',
             'Острый суп из капусты с соевой пастой', 'Овощной суп с клецками', 'Суп с соевой пастой, шпинатом и моллюсками',
             'Стейк из салата латук', 'Жареная куриная грудка с соусом мэнцую майо', 'Удон с тунцом и соленой комбу',
             'Йогуртовый чизкейк с матча', 'Митараси данго с тофу и маття-соусом', 'Митараси данго',
             'Лапша удон с курицей и зеленым луком', 'Крем-суп с зелеными бобами Эдамаме', 'Рыбный мисо суп с тофу')

add_origin(session, list_origin)
add_complexity(session, list_complexity)
add_dish_category(session, list_dish_category)
add_dish(session, list_dish)

session.close()