from datetime import date
from models import Debt
from db import session
from sqlalchemy import or_

def create_debt(debtor_id, indebted_id, amount, currency):
    debt = Debt(
        debtor_id=debtor_id,
        indebted_id=indebted_id,
        amount=amount,
        currency=currency,
        start_date=date.today()
    )

    session.add(debt)
    session.commit()

    return debt

def get_debts_for_user(user_id):
    return session.query(Debt).filter(or_(Debt.debtor_id == user_id, Debt.indebted_id == user_id)).all()
