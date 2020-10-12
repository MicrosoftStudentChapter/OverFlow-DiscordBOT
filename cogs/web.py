import discord
from discord.ext import commands
from googlesearch import search
from Scrappers.stackoverflow import StackOverflow as SO
from Scrappers import compete

class Web(commands.Cog):

    def __init__ (self, client):
        self.client = client

    @commands.command()
    async def google(self, ctx, *, query):
        for result in search(query = query, tld='co.in', lang='en', num=1, start=0, stop=1, pause=1.0):
            await ctx.send(f'{result}')
    
    @commands.command()
    async def error(self, ctx, *, query):
        try :
            for link in search(query = 'stackoverflow what is '+query, tld='co.in', lang='en', num=1, start=0, stop=1, pause=1.0):

                OverFlow = SO(link)
                post = await OverFlow.ScrapContent()
                if post["accepted"]:
                    await ctx.send(f'``` {post["answerContent"]} ``` :white_check_mark: \n :arrow_up: {post["upVotes"]} ')
                else :
                    await ctx.send(f'``` {post["answerContent"]} ``` \n :arrow_up: {post["upVotes"]} ')

        except:
            await ctx.send(f'> Something\'s broken :woozy_face: ! Try modifying your query.')

    @commands.command(aliases = ['cp', 'codechef', 'compete'])
    async def chef(self, ctx):
        '''
        Fetch random problem from Codechef
        '''

        try:
            problem = await compete.get_problem()
            await ctx.send(f'```{problem["problem"]}```\nProblem Link -> {problem["problem_link"]}\n')

        except Exception as e:
            print(e)
            await ctx.send(f'> Something\'s broken :woozy_facy')


def setup(client):
    client.add_cog(Web(client))
