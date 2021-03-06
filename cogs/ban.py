import discord
from discord.ext import commands


class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self,ctx, member: discord.Member):
        if ctx.author.guild_permissions.ban_members:
            await member.ban()
            ban_message = discord.Embed(title='Moderator',
                                    description='User wurde gebannt.',
                                    color=0x00ff00)
            await ctx.send(embed=ban_message)
        else:
            missing_right_message = discord.Embed(title='Error',
                                   description='Dir fehlen die Berechtigungen diesen Befehl zu nutzen.',
                                   color=0xff0000)
            await ctx.send(embed=missing_right_message)

    @ban.error
    async def ban_error(self,ctx, error):
        # Embed for error ,,Member not found'' 
        not_found_message = discord.Embed(title='Error',
                                description='Member konnte nicht gefunden werden.',
                                color=0xff0000)
        # Embed for error ,,Missing Parameter''
        missing_param_message = discord.Embed(title='Error',
                                description='Fehlendes Argument. `ban <Member>`',
                                color=0xff0000)
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=not_found_message)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=missing_param_message)
