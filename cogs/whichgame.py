import random
import discord
from discord.ext import commands


class WhichGameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whichgame(self,ctx):
        games = ["League of Legends",
                 "Among Us",
                 "Osu!",
                 "CS:GO",
                 "Minecraft",
                 "Rocket League",
                 "Valorant",
                 "Krunker.io",
                 "Paladins",
                 "GTA V",
                 "Rainbow Six Siege",
                 "Apex Legends",
                 "World of Warcraft",
                 "Skribbl.io",
                 "Fortnite"]
        game = random.choice(games)
        whichgamemess = discord.Embed(title="Was soll ich spielen?",
                                      description="Hier ein Vorschlag: " + game,
                                      color=0x00ffff)
        await ctx.send(embed=whichgamemess)