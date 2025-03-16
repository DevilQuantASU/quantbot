import discord
from discord import app_commands
from discord.ext import commands
import os
from util.json_manager import JSONManager

class NewsletterStatus(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @app_commands.command(name="statusnewsletter", description="Get the status of the newsletter")
    async def createnewsletter(self, interaction: discord.Interaction):
        json_manager: JSONManager = self.client.json_manager
        data = await json_manager.get_json_file(interaction.guild_id)
        
        if "newsletter" in data:
            await interaction.response.send_message(f"Newsletter has been created") 
        else:
            await interaction.response.send_message(f"No newsletter has been created for this server yet") 
        

async def setup(client: commands.Bot):
    await client.add_cog(NewsletterStatus(client))