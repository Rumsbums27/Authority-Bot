import discord
from discord.ext import commands


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self,ctx):
        help_message = discord.Embed(title='Help',
                                 color=0x00ffff)
        help_message.add_field(name='Command Prefix', value=f'`!`',inline=False)
        help_message.add_field(name='Commands', value='`status` -  Ändert den Status im Nickname\n'
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
                                                  '`rps` - Spiele Schere, Stein, Papier\n'
                                                  '`ssp` - Gleichwertig zu `rps`\n'
                                                  '`schere-stein-papier` - Gleichwertig zu `rps`\n'
                                                  '`whichmovie` - Du weißt nicht, welchen Film du gucken sollst? Dieser Befehl hilft dir\n'
                                                  '`voice` - Läd jemanden zum Private Voice Channel ein\n'
                                                  #'`join` - Spielt Radio in einem Voicechannel\n'
                                                  #'`leave` -  Verlässt den Voicechannel\n'
                           , inline=False)
        help_message.add_field(name='Moderator',value='`clear` - Löscht eine größere Anzahl an Nachrichten\n'
                                                  '`ban` - Bannt einen User\n'
                                                  '`kick` - Kickt einen User\n'
                                                  '`block` - Blockt einen User\n'
                                                  '`unblock` - Entblockt einen User\n'
                                                  '`warn` - Verwarnt einen User\n'
                           , inline=False)
        await ctx.send(embed=help_message)
