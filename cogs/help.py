import discord
from discord.ext import commands
import json

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self,ctx):
        def get_prefix(message,guild):
            with open('./prefixes.json', 'r') as f:
                prefixes = json.load(f)

            return prefixes[str(ctx.guild.id)]

        prefix = get_prefix(message=ctx, guild=None)

        helpmess = discord.Embed(title='Help',
                                 color=0x00ffff)
        helpmess.add_field(name='Command Prefix', value=f'`{prefix}`',inline=False)
        helpmess.add_field(name='Commands', value='`status` -  Ändert den Status im Nickname\n'
                                                  '`nickex` - Gleichwertig zu `status`\n'
                                                  '`userinfo` - Gibt eine Userinfo über den genannten User aus\n'
                                                  '`stats` - Gleichwertig zu `userinfo`\n'
                                                  '`roulette` - Spiele Roulette und versuch dein Glück\n'
                                                  '`clap` - Klatsche voller Ironie\n'
                                                  '`whichgame` - Du weißt nicht, welches Spiel du spielen sollst? Dieser Befehl hilft dir\n'
                                                  '`website` - Gibt dir die URL der Klasse-9k-Website zurück\n'
                                                  '`ping` - Zeigt die Latenz des Bots in Millisekunden\n'
                                                  '`p` - Gleichwertig zu `ping`\n'
                                                  '`report` - Meldet einen User\n'
                                                  '`r` - Gleichwertig zu `report`\n'
                                                  '`vote` -  Führt eine Abstimmung aus\n'
                                                  '`translate` - Übersetzt einen Text\n'
                                                  '`tl` - Gleichwertig zu `translate`\n'
                                                  '`count` - Zeigt die aktuelle Mitgliederzahl von diesem Server\n'
                                                  '`calc` - Führt eine Rechnung aus\n'
                                                  #'`join` - Spielt Radio in einem Voicechannel\n'
                                                  #'`leave` -  Verlässt den Voicechannel'
                           ,inline=False)
        helpmess.add_field(name='Moderator',value='`clear` - Löscht eine größere Anzahl an Nachrichten\n'
                                                  '`ban` - Bannt einen User\n'
                                                  '`kick` - Kickt einen User\n'
                                                  '`block` - Blockt einen User\n'
                                                  '`unblock` - Entblockt einen User\n'
                                                  '`warn` - Verwarnt einen User\n'
                                                  '`points` - Fügt einem User Punkte hinzu'
                           ,inline=False)
        helpmess.add_field(name='Bot-Owner',value='`prefix` - Ändert das Serverprefix')
        await ctx.send(embed=helpmess)
