import discord
from discord.ext import commands
from pymongo import MongoClient
import json


def get_config(config):
    with open('./config.json', 'r') as data:
        configs = json.load(data)
    return configs[str(config)]


cluster = MongoClient(get_config('mongodb'))
db = cluster['authority']
warns_db = db['warn']


class UserInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['stats'])
    async def userinfo(self, ctx, member: discord.Member):
        warns_check = warns_db.find_one({'_id': f'{member}'})
        userinfo = discord.Embed(title="Info",
                                 color=0x00ffff)
        userinfo.add_field(name="Mention", value=member.mention, inline=True)
        userinfo.add_field(name="Name", value=member.name, inline=True)
        userinfo.add_field(name="Nick", value=member.nick, inline=True)
        userinfo.add_field(name="Tag", value=member.discriminator, inline=True)
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

        warns = 0
        if warns_check:
            point = warns_db.find({'_id': f'{member}'})
            for x in point:
                warns = x['how_much']

        blocked = 'False'
        rolle = discord.utils.get(ctx.guild.roles, id=803665577390112828)
        if rolle in member.roles:
            blocked = 'True'

        userinfo.add_field(name='Warns', value=warns, inline=True)
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
