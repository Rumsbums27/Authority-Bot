import discord
from discord.ext import commands


class ClapCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clap(self,ctx, *, arg):
        clapmess = discord.Embed(title='Clap 👏',
                                 description=f'Bravo {arg}. Einfach wow. Einen Applaus bitte. Das hat noch niemand geschafft.',
                                 color=0x00ffff)
        await ctx.send(embed=clapmess)

    @clap.error
    async def clap_error(self,ctx, error):
        claperr = discord.Embed(title='Error',
                                description='Fehlendes Argument. `clap <Member>`',
                                color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=claperr)