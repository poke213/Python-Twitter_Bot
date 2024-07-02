import os
import asyncio
import requests
import json
#create bot

# imports discord lib and dotenv lib
# dotenv is used for getting env without having to call it everyime
import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True


# calls DISCORD_TOKEN to get discord token from .env file
load_dotenv()
TOKEN = os.getenv('phin_key')

client = discord.Client(intents=intents)

# func to pull quotes from website
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return(quote)

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
    
    #inspire quote command
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    
client.run(TOKEN)