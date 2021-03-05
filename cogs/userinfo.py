import discord
from discord.ext import commands
from pymongo import MongoClient


class UserInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['stats'])
    async def userinfo(self, ctx, member: discord.Member):

        cluster = MongoClient('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        db = cluster['authority']
        points_db = db['points']
        warns_db = db['warn']
        reports_db = db['reports']
        point_check = points_db.find_one({'_id': f'{member}'})
        warns_check = warns_db.find_one({'_id': f'{member}'})
        reports_check = reports_db.find_one({'_id': f'{member}'})

        tag = str(member).split('#')[1]
        userinfo = discord.Embed(title="Info",
                                 color=0x00ffff)
        userinfo.add_field(name="Mention", value=member.mention, inline=True)
        userinfo.add_field(name="Name", value=member.name, inline=True)
        userinfo.add_field(name="Nick", value=member.nick, inline=True)
        userinfo.add_field(name="Tag", value=tag, inline=True)
        userinfo.add_field(name="ID", value=member.id, inline=True)
        userinfo.add_field(name='Server beigetreten',
                           value=member.joined_at.strftime(
                               '%d/%m/%Y, %H:%M:%S'),
                           inline=True)
        userinfo.add_field(name='Discord beigetreten',
                           value=member.created_at.strftime(
                               '%d/%m/%Y, %H:%M:%S'),
                           inline=True)
        userinfo.set_thumbnail(url=member.avatar_url)

        points = 0
        warns = 0
        reports = 0
        if point_check:
            point = points_db.find({'_id': f'{member}'})
            for x in point:
                points = x['points']
        if warns_check:
            point = warns_db.find({'_id': f'{member}'})
            for x in point:
                warns = x['how_much']
        if reports_check:
            point = reports_db.find({'_id': f'{member}'})
            for x in point:
                reports = x['reports']

        blocked = 'False'
        rolle = discord.utils.get(ctx.guild.roles, id=803665577390112828)
        if rolle in member.roles:
            blocked = 'True'

        userinfo.add_field(name='Points', value=points, inline=True)
        userinfo.add_field(name='Warns', value=warns, inline=True)
        userinfo.add_field(name='Reports', value=reports, inline=True)
        userinfo.add_field(name='Blocked', value=blocked, inline=True)
        await ctx.send(embed=userinfo)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        # Embed for error ,,Member not found'' 
        not_found_message = discord.Embed(title='Error',
                                     description='Der angegebene Member konnte nicht gefunden werden.',
                                     color=0xff0000)
        # Embed for error ,,Missing Parameter''
        missing_param_message = discord.Embed(title='Error',
                                     description='Fehlendes Argument. `userinfo <Member>`',
                                     color=0xff0000)
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=not_found_message)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=missing_param_message)
