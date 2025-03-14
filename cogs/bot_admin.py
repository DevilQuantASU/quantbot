import discord
from discord.ext import commands 

class BotAdmin(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command(name="synch")
    async def synch(self, ctx):
        try:
            await self.client.tree.sync()
            await ctx.send('Successfully synced command tree. Make sure to press Ctrl+R for the changes to take effect in Discord.')
        except:     
            await ctx.send('Failed to sync command tree, please try again later.')
        

async def setup(client: commands.Bot):
    await client.add_cog(BotAdmin(client))