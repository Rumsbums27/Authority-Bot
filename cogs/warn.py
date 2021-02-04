from pymongo import MongoClient
import discord
from discord.ext import commands

class WarnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self,ctx, user: discord.Member, *, reason):
        cluster = MongoClient('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        db = cluster['authority']
        collection = db['warn']
        embed = discord.Embed(title='Du wurdest verwarnt', color=0xff0000)
        embed.add_field(name='Grund:', value=reason)
        await user.send(embed=embed)
        check = collection.find_one({'_id': f'{user}'})
        if check:
            warns = collection.find({'_id': f'{user}'})
            for x in warns:
                current_warns = x['how_much']
                current_warns += 1
                if current_warns == 3:
                    embed1 = discord.Embed(title='WARNUNG',
                                           description=f'Der Nutzer {user} hat drei Verwarnungen und sollte gekickt oder gebannt werden.',
                                           color=0xff0000)
                    await ctx.send(embed=embed1)
                collection.update_one({'_id': f'{user}'}, {'$set': {'how_much': current_warns}})
                await ctx.send(f'User {user.mention} wurde verwarnt')

        else:
            collection.insert_one({'_id': f'{user}', 'how_much': 1})
            await ctx.send(f'{user.mention} wurde verwarnt')


    @warn.error
    async def warn_error(self,ctx,error):
        warnerr1 = discord.Embed(title='Error',
                                 description='Member konnte nicht gefunden werden.',
                                 color=0xff0000)
        warnerr2 = discord.Embed(title='Error',
                                 description='Fehlendes Argument. `warn <Member>`',
                                 color=0xff0000)
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=warnerr1)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=warnerr2)