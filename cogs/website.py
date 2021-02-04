import discord
from discord.ext import commands

class WebsiteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def website(self,ctx):
        websitemess = discord.Embed(title='Website der Klasse 9k',
                                    description="https://klasse-9k.de",
                                    color=0x00ffff)
        await ctx.send(embed=websitemess)
