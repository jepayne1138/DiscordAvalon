import os
import asyncio
import discord
from discord.ext import commands


COMMAND_CHAR = '/'

bot = commands.Bot(command_prefix=commands.when_mentioned_or(COMMAND_CHAR), description='A playlist example for discord.py')


def run_bot():
    bot.run(os.environ['DISCORD_MUSIC_BOT_TOKEN'])
