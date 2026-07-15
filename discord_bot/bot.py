# geeksforgeeks.org/python/discord-bot-in-python 
# https://www.youtube.com/watch?v=26Sj5hJFqUs

import os
import random

import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True


# On bot initialization
class MyClient(commands.Bot):
    async def on_ready(self):
            print(f"Logged in as a bot {self.user}")

    async def on_message(self, message):
        username = str(message.author).split("#")[0]
        channel = str(message.channel.name)
        user_message = str(message.content)

        #similar to printf(); in C
        print(f'Message {user_message} by {username} on {channel}')

        if message.author == self.user:
            return

        if channel == "general":
            if user_message.lower() == "hello" or user_message.lower() == "hi":
                await message.channel.send(f'Hello {username}')
                return
            elif user_message.lower() == "bye":
                await message.channel.send(f'Bye {username}')
            elif user_message.lower() == "tell me a joke":
                jokes = ["Good morning", "Good evening", "Good night"]
                await message.channel.send(random.choice(jokes))
@client.tree.command(name="hello", description="say heklllo")
async def sayhello(interaction: discord.Interaction):
    await interaction.response.send_message("dih")

client = MyClient(command_prefix="!", intents=intents)
client.run(token)
