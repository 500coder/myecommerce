from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os
from app import app

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

db_user = os.environ['POSTGRES_USER']
db_pass = os.environ['POSTGRES_PASSWORD']
db_name = os.environ['POSTGRES_DB']
host = os.environ['HOST']

DATABASE_URL = f'postgresql://{db_user}:{db_pass}@{host}:5432/{db_name}'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db.init_app(app)

