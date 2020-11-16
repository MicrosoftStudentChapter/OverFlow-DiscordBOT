import os
import random

import discord
from discord.ext import commands


class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hey there !')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'The ping is : {round(self.client.latency * 1000)}ms')

    @commands.command()
    async def clear(self, ctx, amount=5):
        roleCheck = bool(discord.utils.find(lambda role : role.name == os.environ.get('ADMIN'), ctx.author.roles))
        if roleCheck :
            await ctx.channel.purge(limit = amount)
        else :
            await ctx.channel.send('```You don\'t have the rights to access this command```')
    
    @commands.command(aliases = ['8ball']) 
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain', 
                    'It is decidedly so', 
                    'Without a doubt', 
                    'Yes – definitely', 
                    'You may rely on it', 
                    'As I see it, yes', 
                    'Most likely', 
                    'Outlook good', 
                    'Yes Signs point to yes',
                    'I hate to say it, but it is what it is :orz:',
                    'Reply hazy', 
                    'try again', 
                    'Ask again later', 
                    'Better not tell you now', 
                    'Cannot predict now', 
                    'Concentrate and ask again', 
                    'Dont count on it',
                    'Circuit overload.... :skull_crossbones:',
                    'Its.... Impossible',
                    'My reply is no', 
                    'My sources say no', 
                    'Outlook not so good', 
                    'Very doubtful',
                    'I will agree to disagree on that',
                    "I don't think so"]

        await ctx.send(f'Question : {question}\nAnswer : {random.choice(responses)}')


def setup(client):
    client.add_cog(Basic(client))
