from discord.ext import commands
from discord import PermissionOverwrite, Member


class VoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        if after.channel:
            if after.channel.name == 'New Talk':
                public_category = after.channel.category
                public_channel = await after.channel.guild.create_voice_channel(name=f"{member.name}'s Talk",
                                                                                category=public_category)
                await member.move_to(public_channel)

            if after.channel.name == 'New Private Talk':
                overwrites = {
                    after.channel.guild.default_role: PermissionOverwrite(connect=False, view_channel=False),
                    member: PermissionOverwrite(connect=True,
                                                speak=True,
                                                mute_members=True,
                                                deafen_members=True)
                }
                private_category = after.channel.category
                private_channel = await after.channel.guild.create_voice_channel(name=f"{member.name}'s Talk",
                                                                                 category=private_category,
                                                                                 overwrites=overwrites)
                await member.move_to(private_channel)

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
    async def voice(self, ctx, member: Member):
        if ctx.author.voice:
            if ctx.author.voice.channel.category.name == 'Private':
                if ctx.author.name in ctx.author.voice.channel.name:
                    invite = await ctx.author.voice.channel.create_invite(max_age=600, max_uses=1, temporary=True)
                    await member.send(invite)
                    await ctx.author.voice.channel.set_permissions(member, connect=True, view_channel=True, speak=True)
