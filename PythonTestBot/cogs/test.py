

import discord
from discord.ext import commands
from discord import app_commands

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        embedprefix = discord.Embed(
            title="Bot Ping",
            description=f"My Ping is {round(self.bot.latency * 1000)}ms"
        )
        await ctx.send(embed=embedprefix)

    # SLASH
    @app_commands.command(name="ping", description="ping")
    async def _ping(self, ctx: discord.Interaction):
        embedslash = discord.Embed(title="Bot Ping", description=f"ping is {round(self.bot.latency * 1000)}ms")
        await ctx.response.send_message(embed=embedslash)

async def setup(bot: commands.Bot):
    await bot.add_cog(Misc(bot))
