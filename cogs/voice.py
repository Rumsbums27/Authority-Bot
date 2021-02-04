import discord
from discord.ext import commands


class VoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
        if member.bot:
            return

        if after.channel is not None:
            if after.channel.id == 804639684042424320:
                category = after.channel.category
                channel = await after.channel.guild.create_voice_channel(name=f"{member.name}'s Talk",category=category)

                if channel is not None:
                    await member.move_to(channel)

        if before.channel is not None:
            if before.channel.category.id == 804629063569506315:
                if len(before.channel.members) == 0:
                    if before.channel.id == 804639684042424320:
                        pass
                    else:
                        await before.channel.delete()