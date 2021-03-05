import discord
from discord.ext import commands


class ModNewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,ctx):
        mod = self.bot.get_channel(id=798859448868798475)
        news = self.bot.get_channel(id=798851979698634753)

        if ctx.channel == mod:
            news_embed = discord.Embed(title='Authority News',
                                  description=ctx.content,
                                  color=0x00ffff)
            news_embed.set_footer(text="(c) 2020 9k.ist.abgehoben")
            mess = await news.send(embed=news_embed)
            await mess.publish()