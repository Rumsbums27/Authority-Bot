import asyncio
import os

import discord
from discord import Intents
from discord.ext import commands
from cogs import COGS
from pymongo import MongoClient
import json

def get_prefix(guild, message):
    with open('prefixes.json', 'r') as prefix:
        prefixes = json.load(prefix)
    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_prefix,intents=Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Ich bin online')
    bot.loop.create_task(status_task())

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('9k.ist.abgehoben'), status=discord.Status.online)
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game('help'), status=discord.Status.online)
        await asyncio.sleep(5)

for cogs in COGS:
    bot.add_cog(cogs(bot))
    print(f'Successfully activated {cogs}')

#@bot.event
#async def on_member_join(member):
#    cluster = MongoClient(os.environ['MONGO'])
#    db = cluster['authority']
#    collection = db['points']
#    check = collection.find_one({'_id': f'{member}'})
#    if check:
#        point = collection.find({'_id': f'{member}'})
#        for x in point:
#            current_points = 500
#            collection.update_one({'_id': f'{member}'}, {'$set': {'points': current_points}})
#
#    else:
#        collection.insert_one({'_id': f'{member}', 'points': 500})

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    prefixes.pop[str(guild.id)] = '.'

    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

@bot.command()
@commands.is_owner()
async def prefix(ctx,prefix):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

    prefixmess = discord.Embed(
        title='Prefix',
        description=f'Das Serverprefix wurde auf `{prefix}` geändert',
        color=0x00ffff
    )
    await ctx.send(embed=prefixmess)

@prefix.error
async def prefix_error(ctx, error):
    prefixerr = discord.Embed(
        title='Error',
        description='Fehlendes Argument. `prefix <Prefix>`',
        color=0xff0000
    )
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(embed=prefixerr)

bot.run(os.environ["TOKEN"])