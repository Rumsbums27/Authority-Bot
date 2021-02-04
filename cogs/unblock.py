import discord
from discord.ext import commands

class UnBlockCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unblock(self,ctx, member: discord.Member):
        if ctx.author.guild_permissions.kick_members:
            unblockmess1 = discord.Embed(title='Moderator',
                                         description=f'Der Member {member} wurde entblockt.',
                                         color=0xff0000)
            blocked = discord.utils.get(member.guild.roles, id=803665577390112828)
            await ctx.send(embed=unblockmess1)
            await member.remove_roles(blocked)
        else:
            unblockmess2 = discord.Embed(title='Moderator',
                                         description=f'Anscheinend hast du keine Berechtigungen diesen Befehl zu nutzen.',
                                         color=0xff0000)
            await ctx.send(embed=unblockmess2)

    @unblock.error
    async def unblock_error(self,ctx, error):

        unblockerr = discord.Embed(title='Error',
                                   description='Fehlendes Argument. `unblock <Member>`',
                                   color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=unblockerr)