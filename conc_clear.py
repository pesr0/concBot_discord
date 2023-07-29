import discord
from discord.ext import commands
import asyncio

class ConcClear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_role(777305650433622062)
    @commands.command(name="clear")
    async def conc_clear(self, ctx, msg_number: int):
        if msg_number > 30:
            ref = await ctx.send("Vai com calma fera, eu deleto no maximo 30 mensagens por vez")
            await asyncio.sleep(5)
            await ref.delete()
            return

        await ctx.send(f"Mensagens a excluir: {msg_number}")
        await ctx.channel.purge(limit=msg_number + 2)   
        await asyncio.sleep(0)
        ref = await ctx.send("Feito patrão, tudo limpo")
        await asyncio.sleep(5)
        await ref.delete()

async def setup(bot):
    await bot.add_cog(ConcClear(bot))