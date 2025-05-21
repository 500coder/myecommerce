from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

db_user = os.environ['POSTGRES_USER']
db_pass = os.environ['POSTGRES_PASSWORD']
db_name = os.environ['POSTGRES_DB']
host = os.environ['HOST']

DATABASE_URL = f'postgresql://{db_user}:{db_pass}@{host}:5432/{db_name}'



