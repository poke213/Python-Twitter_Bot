import os
import sqlite3
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

# calls DISCORD_TOKEN to get discord token from .env file
load_dotenv()
token = os.getenv('key')
client = commands.Bot(command_prefix = '$', intents=intents)

#lets discord server know bot has entered server
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

# connects to sqlite3 database
conn = sqlite3.connect('groceries.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS groceries (name TEXT, place TEXT, amount INTEGER)')

#add transcation to database
def add_transaction(name, place, amount):
    c.execute('INSERT INTO groceries (name, place, amount) VALUES (?, ?, ?)', (name, place, amount))
    conn.commit()
    
# list transactions from database
def get_transactions(name):
    c.execute('SELECT * FROM groceries WHERE name=?', (name,))
    return c.fetchall()

# reads user input and will output hello
@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@ping.error
async def ping_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments')

#grocieries commands
@client.command()
async def add(ctx, name, place, amount):
    add_transaction(name, place, amount)
    await ctx.send('added to list: ' + name + ' ' + place + ' ' + amount)

@add.error
async def add_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments')
        
@client.command()
async def list(ctx, name):
    transactions = get_transactions(name)
    name_width = 15
    place_width = 40
    amount_width = 30
    if transactions:
        response = "\n".join([
            f"{name[:name_width-3]:<{name_width}} {place[:place_width-3]:<{place_width}} {formatted_amount:>{amount_width}}" 
            if len(name) > name_width or len(place) > place_width else
            f"{name:<{name_width}} {place:<{place_width}} {formatted_amount:<{amount_width}}" 
            for name, place, amount in transactions
            for formatted_amount in [f"${float(amount):.2f}"]
        ])
    else:
        response = "No transactions found"
    await ctx.send(response)

# reads user input and will output hello
@client.event
async def on_message(message):
    # checks if message is from bot
    if message.author == client.user:
        return
    
    # hello
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    #butt
    if message.content.startswith('$butt'):
        await message.channel.send('butt hehe')
    
    # clears all chat    
    if message.content.startswith('$clear'):
        await message.channel.purge(limit=100)
        
    await client.process_commands(message)



client.run(token) # type: ignore