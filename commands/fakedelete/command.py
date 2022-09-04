import random


async def run(message, params):
    rows = int(random.random()*5)+4
    await message.reply(f'Result: {rows} rows deleted from {params[1]}')