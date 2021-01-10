import discord
import os
import random
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix="$") 



@client.command()
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)
@client.command()
async def fuck(ctx):
    await ctx.send("you")

client.run('TOKEN')
