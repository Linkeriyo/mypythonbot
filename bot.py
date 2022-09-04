import discord
from commands.wake import command as wakecommand
from commands.ping import command as pingcommand
import json

configfile = open('files/config.json')
config = json.load(configfile)
token = config['token']
prefix = config['prefix']

intents = discord.Intents.default()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.listening, name='linkeriyo')
client = discord.Client(intents=intents, activity=activity)

@client.event
async def on_ready():
    print('toy vivo')

@client.event
async def on_message(message):
    if message.author.bot:
        return
        
    if not message.content.startswith(prefix):
        return

    content = message.content[len(prefix):]

    words = content.split(" ")

    if len(words) == 0:
        return  

    if words[0] == "wake":
        await wakecommand.run(message, words[1:])
    elif words[0] == "ping":
        await pingcommand.run(message, words[1:])
    else:
        await message.reply('que dices')


client.run(token)
