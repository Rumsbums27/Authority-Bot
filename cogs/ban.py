import discord
from discord.ext import commands


class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self,ctx, member: discord.Member):
        if ctx.author.guild_permissions.ban_members:
            await member.ban()
            banmess = discord.Embed(title='Moderator',
                                    description='User wurde gebannt.',
                                    color=0x00ff00)
            await ctx.send(embed=banmess)
        else:
            banerr = discord.Embed(title='Error',
                                   description='Dir fehlen die Berechtigungen diesen Befehl zu nutzen.',
                                   color=0xff0000)
            await ctx.send(embed=banerr)

    @ban.error
    async def ban_error(self,ctx, error):
        banerr1 = discord.Embed(title='Error',
                                description='Member konnte nicht gefunden werden.',
                                color=0xff0000)
        banerr2 = discord.Embed(title='Error',
                                description='Fehlendes Argument. `ban <Member>`',
                                color=0xff0000)
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=banerr1)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=banerr2)
