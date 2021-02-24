from discord.ext import commands
from discord import PermissionOverwrite,Member

class VoiceCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
#        if member.bot:
#            return

        if after.channel:
            if after.channel.name == 'New Talk':
                category = after.channel.category
                channel = await after.channel.guild.create_voice_channel(name=f"{member.name}'s Talk",
                                                                         category=category)
                if channel:
                    await member.move_to(channel)

            if after.channel.name == 'New Private Talk':
                overwrites = {
                    after.channel.guild.default_role: PermissionOverwrite(connect=False,view_channel=False),
                    member: PermissionOverwrite(connect=True,
                                                speak=True,
                                                mute_members=True,
                                                deafen_members=True)
                }
                category2 = after.channel.category
                channel2 = await after.channel.guild.create_voice_channel(name=f"{member.name}'s Talk",
                                                                          category=category2,
                                                                          overwrites=overwrites)
                if channel2:
                    await member.move_to(channel2)

        if before.channel:
            if before.channel.category.name == 'Voice':
                if len(before.channel.members) == 0:
                    if before.channel.name == 'New Talk':
                        pass
                    else:
                        await before.channel.delete()

            if before.channel.category.name == 'Private':
                if len(before.channel.members) == 0:
                    if before.channel.name == 'New Private Talk':
                        pass
                    else:
                        await before.channel.delete()

    @commands.command()
    async def voice(self,ctx,member:Member):
        if ctx.author.voice:
            if ctx.author.voice.channel.category.name == 'Private':
                if ctx.author.name in ctx.author.voice.channel.name:
                    invite = await ctx.author.voice.channel.create_invite(max_age=600,max_uses=1, temporary=True)
                    await member.send(invite)
                    await ctx.author.voice.channel.set_permissions(member,connect=True,view_channel=True,speak=True)