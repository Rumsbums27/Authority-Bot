import discord
from discord.ext import commands


class ReactionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id == 747888697747308634:
            mitglied = discord.utils.get(
                payload.member.guild.roles, id=559350903141040141)
            if str(payload.emoji) == "✅":
                await payload.member.add_roles(mitglied)
        elif payload.channel_id == 710116001970257973:
            amongus = discord.utils.get(
                payload.member.guild.roles, id=800640785863278643)
            osu = discord.utils.get(
                payload.member.guild.roles, id=799646308285284352)
            lol = discord.utils.get(
                payload.member.guild.roles, id=710089814711468083)
            lor = discord.utils.get(
                payload.member.guild.roles, id=710090605031718993)
            tft = discord.utils.get(
                payload.member.guild.roles, id=710222045824286721)
            wr = discord.utils.get(
                payload.member.guild.roles, id=710222629931581452)
            krunker = discord.utils.get(
                payload.member.guild.roles, id=710222952037089399)
            mc = discord.utils.get(
                payload.member.guild.roles, id=710494243948462271)
            paladins = discord.utils.get(
                payload.member.guild.roles, id=713090663289323611)
            valorant = discord.utils.get(
                payload.member.guild.roles, id=718191255032561805)
            csgo = discord.utils.get(
                payload.member.guild.roles, id=718191138699214869)
            gta = discord.utils.get(
                payload.member.guild.roles, id=749553157427691580)
            rainbow = discord.utils.get(
                payload.member.guild.roles, id=749553249086079017)
            rl = discord.utils.get(
                payload.member.guild.roles, id=749553329943871631)
            xxx = discord.utils.get(
                payload.member.guild.roles, id=710498322531745803)
            musik = discord.utils.get(
                payload.member.guild.roles, id=716022697464955043)
            if str(payload.emoji) == "<:AmongUs:800642346734583838>":
                await payload.member.add_roles(amongus)
            elif str(payload.emoji) == "<:OSU:800641854642061312>":
                await payload.member.add_roles(osu)
            elif str(payload.emoji) == "<:LeagueofLegends:710138275041640458>":
                await payload.member.add_roles(lol)
            elif str(payload.emoji) == "<:LeagueofRunterra:710188280959729716>":
                await payload.member.add_roles(lor)
            elif str(payload.emoji) == "<:TeamfightsTactics:710188281928744960>":
                await payload.member.add_roles(tft)
            elif str(payload.emoji) == "<:WildRift:710188281232359424>":
                await payload.member.add_roles(wr)
            elif str(payload.emoji) == "<:Krunkerio:710188280783568898>":
                await payload.member.add_roles(krunker)
            elif str(payload.emoji) == "<:Minecraft:710494095189213224>":
                await payload.member.add_roles(mc)
            elif str(payload.emoji) == "<:Paladins:713090968810815650>":
                await payload.member.add_roles(paladins)
            elif str(payload.emoji) == "<:Valorant:747897165635911761>":
                await payload.member.add_roles(valorant)
            elif str(payload.emoji) == "<:CSGo:747897167766618132>":
                await payload.member.add_roles(csgo)
            elif str(payload.emoji) == "<:GTAV:747897168081453108>":
                await payload.member.add_roles(gta)
            elif str(payload.emoji) == "<:Rainbow6:747897167359770724>":
                await payload.member.add_roles(rainbow)
            elif str(payload.emoji) == "<:RocketLeague:747897167204843691>":
                await payload.member.add_roles(rl)
            elif str(payload.emoji) == "<:FSK:710498273265188954>":
                await payload.member.add_roles(xxx)
            elif str(payload.emoji) == "🎙️":
                await payload.member.add_roles(musik)

    ########################################################################################################################

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.channel_id == 710116001970257973:
            server = self.bot.get_guild(payload.guild_id)
            nutzer = server.get_member(payload.user_id)
            amongus = discord.utils.get(server.roles, id=800640785863278643)
            osu = discord.utils.get(server.roles, id=799646308285284352)
            lol = discord.utils.get(server.roles, id=710089814711468083)
            lor = discord.utils.get(server.roles, id=710090605031718993)
            tft = discord.utils.get(server.roles, id=710222045824286721)
            wr = discord.utils.get(server.roles, id=710222629931581452)
            krunker = discord.utils.get(server.roles, id=710222952037089399)
            mc = discord.utils.get(server.roles, id=710494243948462271)
            paladins = discord.utils.get(server.roles, id=713090663289323611)
            valorant = discord.utils.get(server.roles, id=718191255032561805)
            csgo = discord.utils.get(server.roles, id=718191138699214869)
            gta = discord.utils.get(server.roles, id=749553157427691580)
            rainbow = discord.utils.get(server.roles, id=749553249086079017)
            rl = discord.utils.get(server.roles, id=749553329943871631)
            xxx = discord.utils.get(server.roles, id=710498322531745803)
            musik = discord.utils.get(server.roles, id=716022697464955043)
            if str(payload.emoji) == "<:AmongUs:800642346734583838>":
                await nutzer.remove_roles(amongus)
            elif str(payload.emoji) == "<:OSU:800641854642061312>":
                await nutzer.remove_roles(osu)
            elif str(payload.emoji) == "<:LeagueofLegends:710138275041640458>":
                await nutzer.remove_roles(lol)
            elif str(payload.emoji) == "<:LeagueofRunterra:710188280959729716>":
                await nutzer.remove_roles(lor)
            elif str(payload.emoji) == "<:TeamfightsTactics:710188281928744960>":
                await nutzer.remove_roles(tft)
            elif str(payload.emoji) == "<:WildRift:710188281232359424>":
                await nutzer.remove_roles(wr)
            elif str(payload.emoji) == "<:Krunkerio:710188280783568898>":
                await nutzer.remove_roles(krunker)
            elif str(payload.emoji) == "<:Minecraft:710494095189213224>":
                await nutzer.remove_roles(mc)
            elif str(payload.emoji) == "<:Paladins:713090968810815650>":
                await nutzer.remove_roles(paladins)
            elif str(payload.emoji) == "<:Valorant:747897165635911761>":
                await nutzer.remove_roles(valorant)
            elif str(payload.emoji) == "<:CSGo:747897167766618132>":
                await nutzer.remove_roles(csgo)
            elif str(payload.emoji) == "<:GTAV:747897168081453108>":
                await nutzer.remove_roles(gta)
            elif str(payload.emoji) == "<:Rainbow6:747897167359770724>":
                await nutzer.remove_roles(rainbow)
            elif str(payload.emoji) == "<:RocketLeague:747897167204843691>":
                await nutzer.remove_roles(rl)
            elif str(payload.emoji) == "<:FSK:710498273265188954>":
                await nutzer.remove_roles(xxx)
            elif str(payload.emoji) == "🎙️":
                await nutzer.remove_roles(musik)
