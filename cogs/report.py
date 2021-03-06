import discord
from discord.ext import commands


class ReportCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['r'])
    async def report(self, ctx, member: discord.Member, reason):
        embed1 = discord.Embed(title='Du wurdest reportet', color=0xff0000)
        embed1.add_field(name='Grund:', value=reason)
        await member.send(embed=embed1)
        reportchannel = self.bot.get_channel(806525815680139304)
        reportmess = discord.Embed(title='User Report',
                                   description=f'{ctx.author} hat {member} gemeldet. Grund: {reason}',
                                   color=0xff0000)
        reportmess.add_field(
            name=f'Originalnachricht von {ctx.author}', value=f'{ctx.message.content}', inline=False)
        await reportchannel.send(embed=reportmess)

    @report.error
    async def report_error(self, ctx, error):
        # Embed for error ,,Member not found'' 
        not_found_message = discord.Embed(title='Error',
                                          description='Der Member konnte nicht gefunden werden.',
                                          color=0xff0000)
        # Embed for error ,,Missing Parameter''
        missing_param_message = discord.Embed(title='Error',
                                              description='Fehlendes Argument. `report <Member> <Grund>`',
                                              color=0xff0000)
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=not_found_message)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=missing_param_message)
