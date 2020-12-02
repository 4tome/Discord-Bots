# Work with Python 3.6
import discord
import random
import requests
import json
import asyncio

TOKEN = 'YOUR TOKEN'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!copy'):

        channel = message.channel

        messages = await channel.history().flatten()
        msg = random.choice(messages)

        while len(msg.content) == 0:
        	msg = random.choice(messages)
        await channel.send(msg.content)


@client.event
async def on_ready():
    print("Running.")
    

client.run(TOKEN)





