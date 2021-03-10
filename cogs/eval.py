import discord
from discord.ext import commands


class ExecCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def execute(self, ctx, *, code):
        run = eval(code)
        embed = discord.Embed(
            title='Execute',
            description=f"```{str(run)}```",
            color=0x00ffff
        )
        await ctx.send(embed=embed)
