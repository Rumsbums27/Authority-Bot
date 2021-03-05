import discord
from discord.ext import commands
from googletrans import Translator


class TranslateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['tl'])
    async def translate(self, ctx, speech, *, arg):
        translator = Translator()
        translation = translator.translate(str(arg), dest=speech).text
        transmess = discord.Embed(title='Translator',
                                  description=translation,
                                  color=0x00ffff)
        await ctx.send(embed=transmess)

    @translate.error
    async def translate_error(self, ctx, error):
        # Embed for error ,,Missing Parameter''
        missing_param_message = discord.Embed(title='Error',
                                 description='Fehlendes Argument. `translate <Ländersprachenabkürzung> <Text>`',
                                 color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=missing_param_message)
