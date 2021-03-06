from pymongo import MongoClient
import discord
from discord.ext import commands
import json


def get_config(config):
    with open('./config.json', 'r') as data:
        configs = json.load(data)
    return configs[str(config)]


cluster = MongoClient(get_config('mongodb'))
db = cluster['authority']
warnings = db['warn']


class WarnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, user: discord.Member, *, reason=None):
        embed = discord.Embed(title='Du wurdest verwarnt', color=0xff0000)
        embed.add_field(name='Grund:', value=reason)
        await user.send(embed=embed)
        check = warnings.find_one({'_id': f'{user}'})
        if check:
            warns = warnings.find({'_id': f'{user}'})
            for x in warns:
                current_warns = x['how_much']
                current_warns += 1
                if current_warns >= 3:
                    warn_embed = discord.Embed(title='WARNUNG',
                                               description=f'Der Nutzer {user} hat {current_warns} Verwarnungen und '
                                                           f'sollte gekickt oder gebannt werden.',
                                               color=0xff0000)
                    await ctx.send(embed=warn_embed)
                warnings.update_one({'_id': f'{user}'}, {
                    '$set': {'how_much': current_warns}})
                await ctx.send(f'User {user.mention} wurde verwarnt')

        else:
            warnings.insert_one({'_id': f'{user}', 'how_much': 1})
            await ctx.send(f'{user.mention} wurde verwarnt')

    @warn.error
    async def warn_error(self, ctx, error):
        # Embed for error ,,Member not found''
        not_found_message = discord.Embed(title='Error',
                                          description='Member konnte nicht gefunden werden.',
                                          color=0xff0000)
        # Embed for error ,,Missing Parameter''
        missing_param_message = discord.Embed(title='Error',
                                              description='Fehlendes Argument. `warn <Member>`',
                                              color=0xff0000)
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=not_found_message)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=missing_param_message)
