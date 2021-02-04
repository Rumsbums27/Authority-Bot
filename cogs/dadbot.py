import discord
from discord.ext import commands


class DadBotCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "i'm" in message.content.lower():
            args = message.content.lower().split("i'm ")[1]
            args2 = args.split(' ')[0]
            await message.channel.send("Hi " + args2 + ", I'm Dad.")
        if "i am" in message.content.lower():
            args = message.content.lower().split("i am ")[1]
            args2 = args.split(' ')[0]
            await message.channel.send("Hi " + args2 + ", I'm Dad.")
        if "i m" in message.content.lower():
            args = message.content.lower().split("i am ")[1]
            args2 = args.split(' ')[0]
            await message.channel.send("Hi " + args2 + ", I'm Dad.")

    async def on_message_edit(self, before, after):
        if "i'm" in after.content.lower():
            args = after.content.lower().split("i'm ")[1]
            args2 = args.split(' ')[0]
            await after.channel.send("Hi " + args2 + ", I'm Dad.")
        if "i am" in after.content.lower():
            args = after.content.lower().split("i am ")[1]
            args2 = args.split(' ')[0]
            await after.channel.send("Hi " + args2 + ", I'm Dad.")
        if "i m" in after.content.lower():
            args = after.content.lower().split("i am ")[1]
            args2 = args.split(' ')[0]
            await after.channel.send("Hi " + args2 + ", I'm Dad.")