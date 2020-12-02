# -*- coding: utf-8 -*-

import discord
import random,string
import asyncio

TOKEN = 'YOUR TOKEN'
client = discord.Client()

async def spam(channel):
    while True:
        await channel.send("".join([random.choice(string.ascii_letters + string.digits) for i in range(random.choice([666, 999, 1212, 1666, 2000]))]))
        await asyncio.sleep(3)


async def bot(channel):
    while True:

        lines = open('p.txt').read().splitlines() #reads from a file filled with quotes and post them every 30 seconds
        myline =random.choice(lines)
        await channel.send(myline)
        await asyncio.sleep(30)

@client.event
async def on_message(message):
    if message.author == client.user:
        if message.content.startswith('!spam'):
    	   client.loop.create_task(spam(message.channel))

#Alternative if autobots don't work anymore
'''
    if message.author == client.user:
        return

    if message.author == CientIdWhoControlTheSpam:
        if message.content.startswith('!spam'):
            spam_txt = "q" * 10 * 20;
            client.loop.create_task(spam(message.channel))
'''

@client.event
async def on_ready():
    print("Running.")
    channel = client.get_channel(494248378126041098) 
    #client.loop.create_task(spam(channel))
    client.loop.create_task(bot(channel))
    


client.run(TOKEN)