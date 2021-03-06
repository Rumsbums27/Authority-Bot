import discord
from discord.ext import commands

class BlockCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def block(self,ctx, member: discord.Member):
        block_message = discord.Embed(title='Moderator',
                                    description=f'Der Member {member} wurde geblockt.',
                                    color=0xff0000)
        blocked = discord.utils.get(member.guild.roles, id=803665577390112828)
        await ctx.send(embed=block_message)
        await member.add_roles(blocked)

    @block.error
    async def block_error(self,ctx, error):
        # Embed for error ,,Missing Parameter''
        block_error_message = discord.Embed(title='Error',
                                 description='Fehlendes Argument. `block <Member>`',
                                 color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=block_error_message)