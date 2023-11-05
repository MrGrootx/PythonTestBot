
import discord
import config, os
from config import TOKEN
from discord.ext import commands


class PyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f"{self.user} is online")

    async def setup_hook(self):
        for fn in os.listdir("cogs"):
            if fn.endswith(".py"):
                await self.load_extension(f"cogs.{fn[:-3]}")
                await self.tree.sync(guild=discord.Object(id="1112106400131330099"))


intents = discord.Intents.default()
intents.message_content = True

bot = PyBot(command_prefix="!", intents=intents)
bot.run(TOKEN)