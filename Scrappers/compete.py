from requests import get
from json import loads
from random import choice
import lxml.html

async def get_problem():
    # Getting Tag list from codechef
    tag_list = loads(get("https://www.codechef.com/get/tags/problems/").content)
    
    # Choosing a random Tag from that tag list !
    tag = choice(tag_list)["tag"]
    
    # Getting Problems with that Speified tag
    problems = loads(get("https://www.codechef.com/get/tags/problems/"+tag).content)["all_problems"]
    
    # Getting a random Problem from that tag
    random_problem_code = choice(list(problems.keys()))
    
    # Getting Problem Link
    problem_link = "https://www.codechef.com/problems/"+random_problem_code
    
    # Getting Body of Problem
    problem = loads(get("https://www.codechef.com/api/contests/PRACTICE/problems/"+random_problem_code).content)["body"]

    # Making Problem Body Clean
    problem = lxml.html.document_fromstring(problem).text_content()
    problem.replace("$","`")

    return {
            "problem": problem,
            "problem_link": problem_link
            }

