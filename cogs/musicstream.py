import discord
from discord.ext import commands


class MusicStreamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self,ctx):
        uservoice = ctx.author.voice
        if uservoice:
            voicechannel = uservoice.channel
            channel = await voicechannel.connect()
            channel.play(discord.FFmpegPCMAudio(source='https://streams.ilovemusic.de/iloveradio1.mp3'))
        else:
            embed = discord.Embed(
                title='Error',
                description='Du musst in einem Voicechannel sein',
                color=0xff0000
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def leave(self,ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
        else:
            embed = discord.Embed(
                title='Error',
                description='Der Bot ist nicht in einem Voicechannel',
                color=0xff0000
            )
            await ctx.send(embed=embed)