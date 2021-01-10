import discord
import os
import random
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix="$") 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$fuck'):
        await message.channel.send('you')

@client.command()
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

client.run('TOKEN')
