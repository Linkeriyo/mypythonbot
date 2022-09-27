import discord
from commands.wake import command as wakecommand
from commands.ping import command as pingcommand
from commands.fakedelete import command as fakedeletecommand
from commands.debt_add import command as adddebtcommand
import db
from models import Debt
import settings

db.Base.metadata.create_all(db.engine)

print("db initialized")

intents = discord.Intents.default()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.listening, name='linkeriyo')
client = discord.Client(intents=intents, activity=activity)

@client.event
async def on_ready():
    print("discord client ready")

@client.event
async def on_message(message):
    if message.author.bot:
        return
        
    if not message.content.startswith(settings.prefix):
        return

    content = message.content[len(settings.prefix):]

    words = content.split(" ")

    if len(words) == 0:
        return  

    if words[0] == "wake":
        await wakecommand.run(message, words[1:])
    elif words[0] == "ping":
        await pingcommand.run(message, words[1:])
    elif words[0] == ";DELETE":
        await fakedeletecommand.run(message, words[1:])
    elif words[0] == "debt":
        await adddebtcommand.run(message, words[1:])
    else:
        await message.reply('que dices')

print("discord client initialized")

client.run(settings.token)
