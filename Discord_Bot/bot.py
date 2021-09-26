import os
import time
import random
from discord.ext import commands
from dotenv import load_dotenv
import vuln_scraper



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
VULNERS_KEY = os.getenv('VULNERS_KEY')

bot = commands.Bot(command_prefix='!')

@bot.command(name='hello')
async def hello(ctx):
    author = ctx.message.author
    username = author.name
    response = f"Hello, {username}"

    
    await ctx.send(response)

@bot.command(name='tellmeabout')
async def scrape_vulns(ctx, search_term):

    scraper = vuln_scraper.VulnScraper()
    response_list = scraper.scrape_mitre(search_term)
   
    counter = 0
    for item in response_list[0]:
        response = item + ": " + response_list[1][counter]
        await ctx.send(response)
        counter +=1
        #take 2 second break to avoid being stopped for spamming
        time.sleep(2)


bot.run(TOKEN)

