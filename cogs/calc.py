import wolframalpha
import discord
from discord.ext import commands

client = wolframalpha.Client('APP-ID')


class CalcCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calc(self, ctx, *, bill):
        response = client.query(bill)
        output = next(response.results).text
        embed = discord.Embed(
            title='Calculator',
            description=f'Das Ergebnis deiner Rechnung: {output}',
            color=0x00ffff
        )
        await ctx.send(embed=embed)

    @calc.error
    async def calc_error(self, ctx, error):
        # Embed for Error ,,Missing Parameter''
        missing_param_message = discord.Embed(title='Error',
                                              description='Fehlendes Argument. `calc <Rechnung>`\n'
                                              'Mögliche Operatoren:\n'
                                              '`+` - Addieren\n'
                                              '`-` - Subtrahieren\n'
                                              '`*` - Multiplizieren\n'
                                              '`\` - Dividieren\n'
                                              '`**`/`^` - Potenzieren\n'
                                              '`sqrt` - Wurzel ziehen',
                                              color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=missing_param_message)
