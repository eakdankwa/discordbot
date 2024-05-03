import os 
import disord
from discord.ext import commands

from dotenv import load_dotenv
_ = load_dotenv()
auth_token = os.environ['discord_token']

intents = discord.Intents.default()
intents.message = True
intents.message_content = True

bot = command.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello there!')

bot.run(auth_token)

