import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

print("initializing db")

engine = db.create_engine(f'sqlite:///elpenco.sqlite')
connection = engine.connect()
metadata = db.MetaData()
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()