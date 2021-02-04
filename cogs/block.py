import discord
from discord.ext import commands

class BlockCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def block(self,ctx, member: discord.Member):
        if ctx.author.guild_permissions.kick_members:
            blockmess1 = discord.Embed(title='Moderator',
                                       description=f'Der Member {member} wurde geblockt.',
                                       color=0xff0000)
            blocked = discord.utils.get(member.guild.roles, id=803665577390112828)
            await ctx.send(embed=blockmess1)
            await member.add_roles(blocked)
        else:
            blockmess2 = discord.Embed(title='Error',
                                       description=f'Anscheinend hast du keine Berechtigungen diesen Befehl zu nutzen.',
                                       color=0xff0000)
            await ctx.send(embed=blockmess2)

    @block.error
    async def block_error(self,ctx, error):

        blockerr = discord.Embed(title='Error',
                                 description='Fehlendes Argument. `block <Member>`',
                                 color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=blockerr)