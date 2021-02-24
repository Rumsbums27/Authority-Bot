import asyncio
import os
import discord
from discord import Intents
from discord.ext import commands
from cogs import COGS, disabled
from pymongo import MongoClient
import json

def get_config(config):
    with open('config.json','r') as data:
        configs = json.load(data)
    return configs[str(config)]

bot = commands.Bot(command_prefix='!',intents=Intents.all())
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
    if cogs in disabled:
        pass
    else:
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

bot.run(get_config('token'))