import os
#create bot

# imports discord lib and dotenv lib
# dotenv is used for getting env without having to call it everyime
import discord
from dotenv import load_dotenv

load_dotenv()

# calls DISCORD_TOKEN to get discord token from .env file
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    
client.run(TOKEN)