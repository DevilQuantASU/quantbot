import discord
from dotenv import load_dotenv
import os
import ssl
import certifi

load_dotenv()
ssl_context = ssl.create_default_context(cafile=certifi.where())

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        print(f"m:{message.content}")
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.environ.get("TOKEN"))
