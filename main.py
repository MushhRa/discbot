import discord
import os
import random
from discord.ext import commands
client = discord.Client()
client = commands.Bot(command_prefix="$") 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

client.run('TOKEN')
