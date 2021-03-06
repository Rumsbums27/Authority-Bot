import discord
from discord.ext import commands


class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self,ctx, member: discord.Member):
        if ctx.author.guild_permissions.kick_members:
            await member.kick()
            kickmess = discord.Embed(title='Moderator',
                                     description='User wurde gekickt.',
                                     color=0x00ff00)
            await ctx.send(embed=kickmess)
        else:
            kickerr = discord.Embed(title='Error',
                                    description='Dir fehlen die Berechtigungen diesen Befehl zu nutzen.',
                                    color=0xff0000)
            await ctx.send(embed=kickerr)

    @kick.error
    async def kick_error(self,ctx, error):
        # Embed for error ,,Member not found'' 
        not_found_message = discord.Embed(title='Error',
                                 description='Member konnte nicht gefunden werden.',
                                 color=0xff0000)
        # Embed for error ,,Missing Parameter''
        missing_param_message = discord.Embed(title='Error',
                                 description='Fehlendes Argument. `kick <Member>`',
                                 color=0xff0000)
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=not_found_message)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=missing_param_message)