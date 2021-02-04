import random
import discord
from discord.ext import commands

class RouletteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roulette(self,ctx, einsatz):
        number = random.randint(0,36)

        winmess = discord.Embed(
            title='Win',
            description=f'Glückwunsch, du hast gewonnen! Die Zahl war {number}',
            color=0x00ff00
        )

        losemess = discord.Embed(
            title='Lose',
            description=f'Schade, du hast verloren. Die Zahl war {number}',
            color=0xff0000
        )

        errmess = discord.Embed(
            title='Error',
            description='Ein Fehler ist aufgetreten.',
            color=0xff0000
        )

        red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        hoch = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        tief = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        gerade = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        ungerade = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

        # Wenn auf schwarz gesetzt ist
        if einsatz.lower() == 'black' or einsatz.lower() == 'schwarz':
            if number in black:
                await ctx.send(embed=winmess)
            else:
                await ctx.send(embed=losemess)

        # Wenn auf rot gesetzt ist
        elif einsatz.lower() == 'red' or einsatz.lower() == 'rot':
            if number in red:
                await ctx.send(embed=winmess)
            else:
                await ctx.send(embed=losemess)

        # Wenn auf tief gesetzt ist
        elif einsatz.lower() == 'tief':
            if number in tief:
                await ctx.send(embed=winmess)
            else:
                await ctx.send(embed=losemess)

        # Wenn auf hoch gesetzt ist
        elif einsatz.lower() == 'hoch':
            if number in hoch:
                await ctx.send(embed=winmess)
            else:
                await ctx.send(embed=losemess)

        # Wenn auf gerade gesetzt ist
        elif einsatz.lower() == 'gerade':
            if number in gerade:
                await ctx.send(embed=winmess)
            else:
                await ctx.send(embed=losemess)

        # Wenn auf ungerade gesetzt ist
        elif einsatz.lower() == 'ungerade':
            if number in ungerade:
                await ctx.send(embed=winmess)
            else:
                await ctx.send(embed=losemess)

        # Wenn auf eine Zahl gesetzt ist
        elif einsatz.isdigit:
            if int(einsatz) <= 36:
                if number == int(einsatz):
                    await ctx.send(embed=winmess)
                else:
                    await ctx.send(embed=losemess)
            else:
                await ctx.send(embed=errmess)

        # Wenn ein Fehler auftritt
        else:
            await ctx.send(embed=errmess)

    @roulette.error
    async def roulette_error(self,ctx, error):
        rouletteerr = discord.Embed(title='Error',
                                     description='Fehlendes Argument. `roulette <schwarz/black>/<rot/red>/<hoch>/<tief>/<gerade>/<ungerade>/<Zahl>`',
                                     color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=rouletteerr)