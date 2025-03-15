import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class MyClient(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$", intents=discord.Intents.all())
        
    async def setup_hook(self):
        for root, _, files in os.walk("./cogs"):
            for filename in files:
                if filename.endswith(".py") and not filename.startswith("__"):
                    # Convert path to a valid module import format
                    rel_path = os.path.relpath(root, "./cogs").replace(os.sep, ".")
                    module_name = f"cogs.{rel_path}.{filename[:-3]}" if rel_path != "." else f"cogs.{filename[:-3]}"
                    
                    await self.load_extension(module_name)
                    print(f"Loaded {module_name}")
         
    async def on_ready(self):
        print('Logged on as', self.user)


client = MyClient()
client.run(os.environ.get("TOKEN"))
