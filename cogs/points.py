from pymongo import MongoClient
import discord
from discord.ext import commands

class PointsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def points(self,ctx, user: discord.Member, points=10):
        cluster = MongoClient('XXXXXXXXXXXXXXXXXXXXX')
        db = cluster['authority']
        collection = db['points']
        embed = discord.Embed(title='Du hast Punkte bekommen', color=0x00ff00)
        embed.add_field(name='Anzahl:', value=points)
        await user.send(embed=embed)
        check = collection.find_one({'_id': f'{user}'})
        if check:
            point = collection.find({'_id': f'{user}'})
            for x in point:
                current_points = x['points']
                current_points += points
                collection.update_one({'_id': f'{user}'}, {'$set': {'points': current_points}})
                await ctx.send(f'Dem User {user.mention} wurden {points} Punkte gegeben.')

        else:
            collection.insert_one({'_id': f'{user}', 'points': points})
            await ctx.send(f'{user.mention} wurden {points} Punkte gegeben')

    @points.error
    async def points_error(self,ctx,error):
        pointserr1 = discord.Embed(title='Error',
                                 description='Member konnte nicht gefunden werden.',
                                 color=0xff0000)
        pointserr2 = discord.Embed(title='Error',
                                 description='Fehlendes Argument. `points <Member> <Anzahl>`',
                                 color=0xff0000)
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=pointserr1)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=pointserr2)