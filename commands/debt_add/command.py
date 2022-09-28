import re
import settings
import db_functions
from funny_data import INSULTS
import random

async def run(message, params):
    clean_message = message.content[len(settings.prefix):]
    match = re.search(r'debt add <@([0-9]+)> x <@([0-9]+)> ([0-9\.,]+) ?([A-z]+)', clean_message)
    indebted_id = match.group(1)
    debtor_id = match.group(2)
    amount = match.group(3)

    if amount.__contains__(','):
        amount.replace(',', '.')
    
    currency = match.group(4)
    
    debt = db_functions.create_debt(indebted_id, debtor_id, amount, currency)

    await message.reply(f'<@{indebted_id}> paga {random.choice(INSULTS).lower()}, id de la deuda: {debt.id}')
