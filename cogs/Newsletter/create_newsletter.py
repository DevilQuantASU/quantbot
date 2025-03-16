import discord
from discord import app_commands
from discord.ext import commands 

class CreateNewsletter(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @app_commands.command(name="createnewsletter", description="Starts or replaces pre-existing newsletter")
    @app_commands.describe(days="How frequently does your newsletter publish?")
    async def createnewsletter(self, interaction: discord.Interaction, days: int):
        await interaction.response.send_message(f"Creating newsletter that updates every, {days} days...") 
        

async def setup(client: commands.Bot):
    await client.add_cog(CreateNewsletter(client))