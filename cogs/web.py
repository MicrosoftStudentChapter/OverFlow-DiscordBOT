import discord
from discord.ext import commands
from googlesearch import search

from Scrappers import compete
from Scrappers.stackoverflow import StackOverflow as SO


class Web(commands.Cog):

    def __init__ (self, client):
        self.client = client

    @commands.command()
    async def google(self, ctx, *, query):
        '''
        Get Google's first search result according to Your Query
        '''
        
        for result in search(query = query, tld='co.in', lang='en', num=1, start=0, stop=1, pause=1.0):
            await ctx.send(f'{result}')
    
    @commands.command()
    async def error(self, ctx, *, query):
        '''
        Get StackOverflow's solution to your query.
        '''
        
        try :
            for link in search(query = 'stackoverflow what is '+query, tld='co.in', lang='en', num=1, start=0, stop=1, pause=1.0):

                OverFlow = SO(link)
                post = await OverFlow.ScrapContent()
                if post["accepted"]:
                    await ctx.send(f'``` {post["answerContent"]} ``` :white_check_mark: \n :arrow_up: {post["upVotes"]} ')
                else :
                    await ctx.send(f'``` {post["answerContent"]} ``` \n :arrow_up: {post["upVotes"]} ')

        except Exception as raised_exception:
            await ctx.send(f'> Something\'s broken :woozy_face: ! Try modifying your query.')
            raise raised_exception

    @commands.command(aliases = ['cp', 'codechef', 'compete'])
    async def chef(self, ctx):
        '''
        (alias = "cp" or "compete" or "codechef") Fetch random problem from Codechef
        '''

        try:
            problem = await compete.get_problem()
            await ctx.send(f'```{problem["problem"]}```\nProblem Link -> {problem["problem_link"]}\n')

        except compete.CodechefTooManyRequests:
            await ctx.send(f'''\n**Too many requests to codechef too fast, please wait a bit !**\n''')

        except Exception as raised_exception:
            await ctx.send(f'> Something\'s broken :woozy_face: !')
            raise raised_exception

def setup(client):
    client.add_cog(Web(client))
