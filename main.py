import discord
from discord.ext import commands
TOKEN =''

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async  def on_ready ():
    print(f"{client.user} has connect to discord")

@client.command()
async  def hello_goodbye(ctx):
    await ctx.send("Hello there !")

client.run(TOKEN) 