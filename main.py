import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class MyClient(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$", intents=discord.Intents.all())
        
    async def setup_hook(self):
       for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("__"):
                await self.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded {filename}")
         
    async def on_ready(self):
        print('Logged on as', self.user)


client = MyClient()
client.run(os.environ.get("TOKEN"))
