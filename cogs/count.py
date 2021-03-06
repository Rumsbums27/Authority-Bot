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
        for i in guild.members:
            count += 1

        count_message = discord.Embed(title='Counter',
                                  description=f'Aktuell gibt es {count} Members auf diesem Server',
                                  color=0x00ffff)
        await ctx.send(embed=count_message)
        await counter.edit(name=f'Member: {count}')