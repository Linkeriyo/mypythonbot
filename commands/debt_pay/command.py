import re
import settings
import db_functions
import discord.ui
import db_functions
import discord

async def run(message, params):
    clean_message = message.content[len(settings.prefix):]
    
    debts = db_functions.get_debts_for_user(message.author.id)
    options = []

    for d in debts:
        options.add(discord.SelectOption(label=f'Debt {d.id}', description=str(d)))

    await message.reply(options)
