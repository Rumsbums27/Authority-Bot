import discord
from discord.ext import commands


class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,arg):
        if arg.isdigit():
            count = int(arg) + 1
            await ctx.channel.purge(limit=count)

    @clear.error
    async def clear_error(self,ctx,error):
        # Embed for Error ,,Missing Parameter''
        missing_param_message = discord.Embed(title='Error',
                                 description='Fehlendes Argument. `clear <Anzahl>`',
                                 color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=missing_param_message)
