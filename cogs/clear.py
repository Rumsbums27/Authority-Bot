import discord
from discord.ext import commands


class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self,ctx,arg):
        if ctx.author.permissions_in(ctx.channel).manage_messages:
            if arg.isdigit():
                count = int(arg) + 1
                await ctx.channel.purge(limit=count)

    @clear.error
    async def clear_error(self,ctx,error):
        clearerr = discord.Embed(title='Error',
                                 description='Fehlendes Argument. `clear <Anzahl>`',
                                 color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=clearerr)
