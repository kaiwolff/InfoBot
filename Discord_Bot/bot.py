import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='hello')
async def nine_nine(ctx):
    author = ctx.message.author
    username = author.name
    response = f"Hello, {username}"

    
    await ctx.send(response)

bot.run(TOKEN)

