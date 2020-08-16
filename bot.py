import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

clientId = os.environ.get('CLIENT')

client = commands.Bot(command_prefix='!')

cogs = [
    'initialize',
    'roles',
    'web',
    'basic'
]

for cog in cogs :
    client.load_extension(f'cogs.{cog}')

client.run(clientId)