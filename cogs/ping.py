import discord
from discord.ext import commands

class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['p'])
    async def ping(self,ctx):
        ping = int(self.bot.latency * 1000)
        color = 0x00ffff
        if ping >= 1000:
            color = 0x000000
        elif ping >= 100:
            color = 0xff0000
        elif ping >= 10:
            color = 0xff8000
        elif ping < 10:
            color = 0x00ff00
        pingmess = discord.Embed(title='Ping',
                                 description=f'Die Latenz beträgt {ping}ms',
                                 color=color)
        await ctx.send(embed=pingmess)