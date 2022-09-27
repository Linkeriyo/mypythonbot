import re
import settings
import db

async def run(message, params):
    clean_message = message.content[len(settings.prefix):]
    match = re.search(r'debt add <@([0-9]+)> x <@([0-9]+)>', clean_message)
    await message.reply(f'indebted: <@{match.group(1)}>, debtor: <@{match.group(2)}>')
