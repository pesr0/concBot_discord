import discord
from discord.ext import commands

class ConcEcho(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_role(777305650433622062)
    @commands.command(name="echo")
    async def conc_echo(self, ctx, msg_input: str):
        await ctx.send(msg_input)

async def setup(bot):
    await bot.add_cog(ConcEcho(bot))
