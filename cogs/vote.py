import discord
from discord.ext import commands

class VoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vote(self,ctx, *, arg):
        await ctx.message.delete()
        votemess1 = discord.Embed(title='Voting',
                                  description=arg,
                                  color=0x00ffff)
        votemess2 = await ctx.send(embed=votemess1)
        await votemess2.add_reaction('👍')
        await votemess2.add_reaction('👎')

    @vote.error
    async def vote_error(self,ctx, error):
        voteerr = discord.Embed(title='Error',
                                description='Fehlendes Argument. `vote <Abstimmung>`',
                                color=0xff0000)

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=voteerr)