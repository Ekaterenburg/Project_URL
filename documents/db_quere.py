import sqlalchemy as sq
import os
from sqlalchemy.orm import sessionmaker
from models import *

base_name = 'baza'
DSN = f'sqlite:///{base_name}'
engine = sq.create_engine(DSN)
create_table(engine)