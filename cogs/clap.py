import discord
from discord.ext import commands


class ClapCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clap(self,ctx, *, arg):
        clap_message = discord.Embed(title='Clap 👏',
                                 description=f'Bravo {arg}. Einfach wow. Einen Applaus bitte. Das hat noch niemand geschafft.',
                                 color=0x00ffff)
        await ctx.send(embed=clap_message)

    @clap.error
    async def clap_error(self,ctx, error):
        # Embed for Error ,,Missing Parameter''
        missing_param_message = discord.Embed(title='Error',
                                description='Fehlendes Argument. `clap <Member>`',
                                color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=missing_param_message)