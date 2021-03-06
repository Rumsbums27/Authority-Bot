import discord
from discord.ext import commands


class VoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vote(self, ctx, *, arg):
        await ctx.message.delete()
        vote_embed = discord.Embed(title='Voting',
                                   description=arg,
                                   color=0x00ffff)
        vote_message = await ctx.send(embed=vote_embed)
        await vote_message.add_reaction('👍')
        await vote_message.add_reaction('👎')

    @vote.error
    async def vote_error(self, ctx, error):
        # Embed for error ,,Missing Parameter''
        missing_param_message = discord.Embed(title='Error',
                                              description='Fehlendes Argument. `vote <Abstimmung>`',
                                              color=0xff0000)

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=missing_param_message)
