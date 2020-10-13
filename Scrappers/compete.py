import re
from json import loads
from json.decoder import JSONDecodeError
from random import choice

import httpx
import lxml.html


class CodechefTooManyRequests(Exception):
    pass


def replace(string, substitutions):

    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)


async def get_problem():
    async with httpx.AsyncClient(timeout=20.0) as client:
        try:
            # Getting Tag list from codechef
            tag_response = await client.get("https://www.codechef.com/get/tags/problems/")
            tag_list = loads(tag_response.content)
            
            # Choosing a random Tag from that tag list !
            tag = choice(tag_list)["tag"]
            
            # Getting Problems with that Speified tag
            problem_list_response = await client.get("https://www.codechef.com/get/tags/problems/"+tag)
            problem_list = loads(problem_list_response.content)["all_problems"]
            
            # Getting a random Problem from that tag
            random_problem_code = choice(list(problem_list.keys()))
            
            # Getting Problem Link
            problem_link = "https://www.codechef.com/problems/"+random_problem_code
            
            # Getting Body of Problem
            problem_response = await client.get("https://www.codechef.com/api/contests/PRACTICE/problems/"+random_problem_code)
            problem = loads(problem_response.content)["body"]

        except JSONDecodeError as exception:
            raise CodechefTooManyRequests from exception

    # Making Problem Body Clean
    problem = lxml.html.document_fromstring(problem).text_content()

    max_message_length = 1900
    if len(problem) >= max_message_length:
        problem = problem[:max_message_length] + "\n.\n.\n."
    
    replace_table = {
                "\\leq": "<=",
                "\\geq": ">=",
                "\\le": "<",
                "\\ge": ">",
                "\\eq": "=",
                "$": "",
            }

    problem = replace(problem, replace_table)

    

    return {
            "problem": problem,
            "problem_link": problem_link,
            }

