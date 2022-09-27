import db
from sqlalchemy import Column, Integer, String, Float, Date

class Debt(db.Base):
    __tablename__ = 'debt'

    id = Column(Integer, primary_key=True)
    debtor_id = Column(Integer, nullable=False)
    indebted_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    due_date = Column(Date)
    paid_date = Column(Date)

