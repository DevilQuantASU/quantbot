import discord
from dotenv import load_dotenv
import os

load_dotenv()

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.tree = discord.app_commands.CommandTree(self)
        
    async def on_ready(self):
        print('Logged on as', self.user)
        await self.tree.sync(guild=discord.Object(id=1340933447891554385))
        
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == '$sync':
            try:
                await self.tree.sync()
                await message.channel.send('Successfully synced command tree. Make sure to press Ctrl+R for the changes to take effect in Discord.')
            except:     
                await message.channel.send('Failed to sync command tree, please try again later.')


client = MyClient()

@client.tree.command(name="ping", description="Replies with Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


client.run(os.environ.get("TOKEN"))
