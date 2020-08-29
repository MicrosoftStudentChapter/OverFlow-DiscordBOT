from bs4 import BeautifulSoup
import requests


"""for link in search(query = 'stackoverflow C++ Segmentation fault', tld='co.in', lang='en', num=1, start=0, stop=1, pause=1.0):

    REQUEST = requests.get(link)

    BS = BeautifulSoup(REQUEST.text, 'html.parser')

    Post = BS.select('.post-text')[1].getText()

    print(Post)"""

class StackOverflow () :

    def __init__(self, link):
      self.link = link

    def ScrapContent (self) :
        REQUEST = requests.get(self.link)
        responseText = REQUEST.text

        SOUP = BeautifulSoup(responseText, 'html.parser')
        
        answerBlock = SOUP.select('#answers')[0]

        answerContent = answerBlock.select('.js-post-body')[0].getText()
        upVotes = answerBlock.select('.js-vote-count')[0].getText()
        accepted = bool(answerBlock.find('div', class_='accepted-answer'))

        post = {
            'answerContent': answerContent,
            'upVotes': upVotes,
            'accepted': accepted
        }

        return post