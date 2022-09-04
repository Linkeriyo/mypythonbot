import discord
from wol import send_magic_packet
import json

configfile = open('files/config.json')
config = json.load(configfile)
token = config['token']
prefix = config['prefix']

intents = discord.Intents.default()
intents.message_content = True

activity = discord.ActivityType.listening, name="linkeriyo"
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
        try:
            if not words[1]:
                await message.reply("¿QUÉ?")
                return

            if send_magic_packet(words[1]):
                await message.reply("enviado")
            else:
                await message.reply("no puc")
        except:
            await message.reply("¿QUÉ?")


client.run(token)
