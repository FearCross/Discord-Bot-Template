import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

# importing libs

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix=';', intents=intents)

# giving bot configs


@client.event
async def on_ready():
    print('The bot is ready to get started.')
    print('--------------------------------')

# making the bot works

@client.command()
async def cross(ctx):
    await ctx.send("Here is your code, you can use whatever you want.")

# to create another command all you need to do is just copy and paste @client.command()

@client.command()
async def chat(ctx):
    await ctx.send("Hey, I'm on the chat.")

#creating commands (you can clone this command afterwards)
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)

@client.event
async def on_member_join(member):
    await member.send('Hello, welcome to our test server.')

    # I'm working on this still.

# for this method you should create a token.py or whatever you want to put your token
    
