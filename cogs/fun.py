import asyncio
import os
import random

import aiohttp
import asyncpraw
import discord

from discord import app_commands
from discord.ext import commands

reddit = asyncpraw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent="Scripty",
)


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Flip a coin")
    async def flip(self, interaction: discord.Interaction):
        await interaction.response.defer()
        coin = ["Heads", "Tails"]
        embed = discord.Embed(
            title="Flip", description=random.choice(coin), color=discord.Color.blurple()
        )
        await interaction.followup.send(embed=embed)

    @app_commands.command(description="The hottest Reddit r/memes")
    async def meme(self, interaction: discord.Interaction):
        await interaction.response.defer()

        # subreddit = await reddit.subreddit("memes", fetch=True)
        # submissions = []
        # async for submission in subreddit.hot(limit=3):
        #     submissions.append(submission)
        # random_submission = random.choice(submissions)
        async with aiohttp.ClientSession() as session:
            reddit_url = "https://reddit.com/r/memes/hot.json"
            async with session.get(reddit_url) as response:
                reddit = await response.json()
                print(reddit["data"]["children"])

        # def get_reddit():
        #     try:
        #         base_url = f"https://reddit.com/r/memes/hot.json"
        #         request = requests.get(base_url, headers = {"User-Agent": "Scripty"})
        #     except Exception as error:
        #         print(error)
        #     return request.json()

        # r = get_reddit()
        # submissions = []
        # for submission in r["data"]["children"]:
        #     submissions.append(r["data"]["children"])

        # random_submission = random.choice(submissions)
        # embed = discord.Embed(
        #     title=random_submission["title"],
        #     url=f"https://reddit.com{random_submission['permalink']}",
        # )
        # embed.set_image(url=random_submission["url"])

        # await interaction.followup.send(embed=embed)

    @app_commands.command(description=";)")
    async def rickroll(self, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.followup.send("https://youtu.be/dQw4w9WgXcQ")


async def setup(bot):
    await bot.add_cog(Fun(bot))
