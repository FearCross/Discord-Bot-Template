import discord
from discord.ext import commands
from config import token

# importing libs

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=';', intents=intents)

# giving bot configs


@client.event
async def on_ready():
    print('The bot is ready to get started.')
    print('--------------------------------')

# making the bot works

@client.command()
async def cross(ctx):
    await ctx.send("Here is your code, you can use whatever you want")

#creating commands (you can clone this command afterwards)

client.run(token)

# for this method you should create a token.py or whatever you want to put your token
    
