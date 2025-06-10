import os
import discord
from discord.ext import commands

# Set the required intents
intents = discord.Intents.default()
intents.message_content = True  # Allow bot to read messages

# Create the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

# Use the token from the environment variable
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
