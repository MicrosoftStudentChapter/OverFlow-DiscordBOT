import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

messageIdentity = os.environ.get('ROLE_MESSAGE_ID')

class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        messageId = payload.message_id
        if messageId == int(messageIdentity):
            guildId = payload.guild_id
            guild = discord.utils.find(lambda G : G.id == guildId, self.client.guilds)

            role = discord.utils.get(guild.roles, name = payload.emoji.name)
            
            if role is not None :
                member = discord.utils.find(lambda mem : mem.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                else:
                    None

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        messageId = payload.message_id
        if messageId == int(messageIdentity):
            guildId = payload.guild_id
            guild = discord.utils.find(lambda G : G.id == guildId, self.client.guilds)

            role = discord.utils.get(guild.roles, name = payload.emoji.name)

            if role is not None :
                member = discord.utils.find(lambda mem : mem.id == payload.user_id, guild.members)
                if member is not None :
                    await member.remove_roles(role)
                else :
                    None

def setup(client):
    client.add_cog(Roles(client))