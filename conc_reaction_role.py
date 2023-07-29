import discord
from discord.ext import commands
import asyncio


class ConcReactionRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="role")
    async def conc_reaction_role(self, ctx):
        try:
            message = await ctx.fetch_message("1130961251028193340-1133141445147115520")
        except discord.NotFound:
            return await ctx.send("Mensagem não encontrada. Verifique o ID e se o bot tem acesso à mensagem.")
        
        def check(reaction, user):
            return user != ctx.user and reaction.message.id == message.id

        try:
            reaction, user = await ctx.wait_for('reaction_add', check=check, timeout=60)
        except asyncio.TimeoutError:
         await ctx.send("Nenhuma reação recebida a tempo.")
        else:
            await ctx.send(f'Usuário {user.mention} reagiu à mensagem!')
        

async def setup(bot):
    await bot.add_cog(ConcReactionRole(bot))