import os
import asyncio
#create bot

# imports discord lib and dotenv lib
# dotenv is used for getting env without having to call it everyime
import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True


# calls DISCORD_TOKEN to get discord token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client(intents=intents)

#lets discord server know bot has entered server
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    
# reads user input and will outputt hello
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$butt'):
        await message.channel.send('butt hehe')
    
client.run(TOKEN)