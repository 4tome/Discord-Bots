# Work with Python 3.6
import discord
import random
import requests
import json
import asyncio

TOKEN = 'YOUR TOKEN'

client = discord.Client()

API_ENDPOINT = "https://api.twitch.tv/helix/streams?user_login=USUARIO"

headers = {
    'Client-ID': "CLIENT ID"
    }

async def is_live(channel, live):
    while True:
        await client.wait_until_ready()

        if channel == None:
            print("Wrong channel ID")
            return True

        print(channel)
        r = requests.get(url = API_ENDPOINT, headers = headers)

        
        try:
            data_json = json.loads(r.text)['data']
        
        except KeyError:
            print("Exception")

        if not data_json:
            live = False
        else:

            if live == True:
                print("Desconectado")
                await asyncio.sleep(30)
                continue
            else:
                print("Live")
                game_id = data_json[0]['game_id']
                title = data_json[0]['title']
                user_name = data_json[0]['user_name']

                line = "Directito de " + user_name + "\n\n" + title + "\n" + "https://www.twitch.tv/USER/"
                await channel.send(line)
                live = True

        await asyncio.sleep(30)
        


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!detalle'): #!user

        channel = message.channel

        messages = ["message","message2","message3"]
        msg = random.choice(messages)

        await channel.send(msg)


@client.event
async def on_ready():
    print("Running.")
    live = False
    channel = client.get_channel(CHANNEL_ID)
    client.loop.create_task(is_live(channel, live))

client.run(TOKEN)




