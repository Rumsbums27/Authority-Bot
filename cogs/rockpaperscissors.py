import discord
from discord.ext import commands
from random import choice

class RockPaperScissorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ssp','schere-stein-papier'])
    async def rps(self,ctx,arg):
        computer = choice(['Schere','Stein','Papier'])

        win = discord.Embed(
            title='Win',
            description=f'Du hast mit **{arg}** gegen den Bot mit **{computer}** gewonnen',
            color=0x00ff00
        )

        lose = discord.Embed(
            title='Lose',
            description=f'Du hast mit **{arg}** gegen den Bot mit **{computer}** verloren',
            color=0xff0000
        )

        tie = discord.Embed(
            title='Tie',
            description=f'Du hast ein Unentschieden mit **{arg}**',
            color=0x00ffff
        )

        # If the computer has 'Schere'
        if computer == 'Schere' and arg.lower() == 'stein':
            await ctx.send(embed=win)
        elif computer == 'Schere' and arg.lower() == 'papier':
            await ctx.send(embed=lose)
        elif computer == 'Schere' and arg.lower() == 'schere':
            await ctx.send(embed=tie)

        # Else if the computer has 'Stein'
        elif computer == 'Stein' and arg.lower() == 'papier':
            await ctx.send(embed=win)
        elif computer == 'Stein' and arg.lower() == 'schere':
            await ctx.send(embed=lose)
        elif computer == 'Stein' and arg.lower() == 'stein':
            await ctx.send(embed=tie)

        # Else if the computer has 'Papier'
        elif computer == 'Papier' and arg.lower() == 'schere':
            await ctx.send(embed=win)
        elif computer == 'Papier' and arg.lower() == 'stein':
            await ctx.send(embed=lose)
        elif computer == 'Papier' and arg.lower() == 'papier':
            await ctx.send(embed=tie)

    @rps.error
    async def roulette_error(self, ctx, error):
        rpserr = discord.Embed(title='Error',
                                    description='Fehlendes Argument. `rps <Hand>`',
                                    color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=rpserr)
