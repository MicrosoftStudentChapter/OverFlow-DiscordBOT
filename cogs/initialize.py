import discord
from discord.ext import commands


class Initialize(commands.Cog):

    def __init__ (self, client):
        self.client = client
        self.welcomeMessage = "Welcome to Microsoft Learn Student Chapter's Open Source Community. \nWe are elated to have you on board with us. \nHope you have a memorable experience with us. \nRegards, \n**Microsoft Learn Student Chapter**"

    ver = '1.0.1'

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity = discord.Game('MLSC OpenSource'))
        print(f'{self.client.user} is ready !')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(f'Hey **{member.name}**! {self.welcomeMessage}')

    @commands.command()
    async def version(self, ctx):
        await ctx.send(f'```The current bot version is v{self.ver}```')

def setup(client):
    client.add_cog(Initialize(client))