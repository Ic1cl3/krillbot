import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

quickcommands = {}
with open('data/quickcommands.txt', 'r') as f:
    for line in f:
        quickcommands[line.strip().split('##')[0]] = line.strip().split('##')[1]

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"yayy i'm {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    for command, response in quickcommands.items():
        if message.content.startswith(command):
            await message.channel.send(response)
            return

bot.run(token, log_handler=handler, log_level=logging.DEBUG)