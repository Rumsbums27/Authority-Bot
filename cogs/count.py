import discord
from discord import Guild
from discord.ext import commands


class CountCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def count(self,ctx):
        guild: Guild = ctx.guild
        count = 0
        counter = self.bot.get_channel(804242511634759681)
        for members in guild.members:
            count += 1

        countmess = discord.Embed(title='Counter',
                                  description=f'Aktuell gibt es {count} Members auf diesem Server',
                                  color=0x00ffff)
        await ctx.send(embed=countmess)
        await counter.edit(name=f'Member: {count}')