import os

import discord

from discord import app_commands
from discord.ext import commands

guild_id = os.environ["GUILD_ID"]


class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Display the help interface")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.defer()
        embed = discord.Embed(
            title="Help",
            description="Post Traumatic Ship Disorder is real. Please contact Dr. Hrishikesh Kondiboyina PhD Psychology as soon as possible.",
            color=discord.Color.blurple(),
        )
        await interaction.followup.send(embed=embed)

    @app_commands.command(description="Replies with PyGoose bot invite")
    async def invite(self, interaction: discord.Interaction):
        await interaction.response.defer()
        embed = discord.Embed(
            title="Invite",
            description="Invite PyGoose to your Discord Server!",
            color=discord.Color.blurple(),
        )
        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label="Add to Server",
                url="https://discord.com/api/oauth2/authorize?client_id=861341470904942622&permissions=8&scope=bot%20applications.commands",
            )
        )
        await interaction.followup.send(embed=embed, view=view)

    @app_commands.command(description="Replies with bot latency")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.defer()
        embed = discord.Embed(
            title="Ping",
            description=f"Pong! `{round(interaction.client.latency * 1000)}ms`",
            color=discord.Color.blurple(),
        )
        await interaction.followup.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Bot(bot))
