import os

import discord

from discord.ext import commands


token = os.environ["STAGING"]
guild_id = os.environ["GUILD_ID"]

intents = discord.Intents.default()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="", intents=intents, activity=discord.Game(name="/help")
        )

    async def startup(self):
        await self.wait_until_ready()
        print(f"Ready! Initialized client as {bot.user}.")
        await self.tree.sync()
        await self.tree.sync(guild=discord.Object(id=guild_id))
        print("Successfully synced global & staging application commands.")

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")

        self.loop.create_task(self.startup())


bot = Bot()


bot.run(token)
