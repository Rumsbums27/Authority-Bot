import discord
from discord.ext import commands


class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['nickex'])
    async def status(self, ctx, *, arg):
        toolong_error = discord.Embed(title='Error',
                                description='Extension zu lang. Der gesamte Nickname darf nicht länger als 32 Zeichen sein.',
                                color=0xff0000)
        if ctx.author.nick == None:
            if len(ctx.author.name + " [" + arg + "]") <= 32:
                if "[" and "]" in ctx.author.name:
                    ex = ctx.author.name.split("[")[1]
                    nick = ctx.author.nick.replace(ex, arg + "]")
                    await ctx.author.edit(nick=nick)
                else:
                    nick = f'{ctx.author.name} [{arg}]'
                    await ctx.author.edit(nick=nick)
            else:
                await ctx.send(embed=toolong_error)
        else:
            base_nick = ctx.author.nick.split(" [")[0]
            if len(f'{base_nick}  [{arg}]') <= 32:
                if "[" and "]" in ctx.author.nick:
                    ex = ctx.author.nick.split("[")[1]
                    nick = ctx.author.nick.replace(ex, f'{arg}]')
                    await ctx.author.edit(nick=nick)
                else:
                    nick = f'{ctx.author.nick} [{arg}]'
                    await ctx.author.edit(nick=nick)
            else:
                await ctx.send(embed=toolong_error)

    @status.error
    async def status_error(self, ctx, error):
        # Embed for error ,,Missing Parameter''
        missing_param_message = discord.Embed(title='Error',
                                  description='Fehlendes Argument. `status <Extension>`',
                                  color=0xff0000)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=missing_param_message)
