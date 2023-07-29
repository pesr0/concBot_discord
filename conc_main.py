import discord
import asyncio
from discord.ext import commands
import asyncio
import nacl

prefix = "."

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

async def load_extensions():
    extensions = ["conc_echo", "conc_clear", "conc_play", "conc_reaction_role", "conc_test"]
    for ext in extensions:
        await bot.load_extension(ext)

async def main():
    async with bot:
        await load_extensions()
        await bot.start("APITOKEN")

asyncio.run(main())