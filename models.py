import db
from sqlalchemy import Column, Integer, String, Float, Date

class Debt(db.Base):
    __tablename__ = 'debt'

    id = Column(Integer, primary_key=True)
    debtor_id = Column(Integer, nullable=False)
    debtor_name = Column(String)
    indebted_id = Column(Integer, nullable=False)
    indebted_name = Column(String)
    amount = Column(Float, nullable=False)
    currency = Column(String)
    start_date = Column(Date, nullable=False)
    due_date = Column(Date)
    paid_date = Column(Date)

    def __str__(self):
        return f'{self.indebted_name} owes {self.amount} {self.currency} to {self.debtor_name}.'
