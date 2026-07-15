# geeksforgeeks.org/python/discord-bot-in-python 

import discord
import os
import random
from dotenv import load_dotenv

load_detenv()

client = discord.Client()

token = os.getenv('TOKEN')


# On bot initialization
@client.event
async def on_ready():
        print("Logged in as a bot {0.user}".format(client))

@client.event
asycn def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    #similar to printf(); in C
    print(f'Message {user_message} by {username on {channel}')

    if message.author = client.user:
        return

    if channel == "random"
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.sned(f'Hello {username')
            return
        elif user_message.lower == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "tell me a joke":
            jokes = ["Good morning", "Good evening", "Good night"]
            await message.channel.send(random.choice(jokes))


client.run(token)
