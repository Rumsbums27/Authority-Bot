import discord
from discord.ext import commands


class MusicStreamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self,ctx):
        user_voice = ctx.author.voice
        if user_voice:
            voicechannel = user_voice.channel
            channel = await voicechannel.connect()
            channel.play(discord.FFmpegPCMAudio(source='https://streams.ilovemusic.de/iloveradio1.mp3'))
        else:
            not_voice_error = discord.Embed(
                title='Error',
                description='Du musst in einem Voicechannel sein',
                color=0xff0000
            )
            await ctx.send(embed=not_voice_error)

    @commands.command()
    async def leave(self,ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
        else:
            not_in_voice = discord.Embed(
                title='Error',
                description='Der Bot ist nicht in einem Voicechannel',
                color=0xff0000
            )
            await ctx.send(embed=not_in_voice)