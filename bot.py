import asyncio
import discord
from discord import Intents, Embed
from discord.ext import commands
from cogs import COGS, disabled
import json


def get_config(config):
    with open('config.json', 'r') as data:
        configs = json.load(data)
    return configs[str(config)]


bot = commands.Bot(command_prefix='!', intents=Intents.all())
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


@bot.event
async def on_command_error(ctx, error):
    embed = Embed(
        title='Error',
        description=str(error),
        color=0xff0000
    )
    await ctx.send(embed=embed)

for cogs in COGS:
    if cogs in disabled:
        pass
    else:
        bot.add_cog(cogs(bot))
        print(f'Successfully activated {cogs}')


bot.run(get_config('token'))
