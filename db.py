from datetime import date
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

print("initializing db")

engine = sqlalchemy.create_engine(f'sqlite:///elpenco.sqlite')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
