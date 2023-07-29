import discord
from discord.ext import commands


class ConcTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def conc_connecet(self, ctx):
        await ctx.send("funcao chamada")
        channel = ctx.author.voice.channel
        await channel.connect()


async def setup(bot):
    await bot.add_cog(ConcTest(bot))
