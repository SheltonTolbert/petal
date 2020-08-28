import praw
import time
from bs4 import BeautifulSoup as bs
import urllib.request
import sys
import requests
from datetime import datetime


class Post():

    def __init__(self, title, author, link, score, time):
        self.title = title
        self.author = author
        self.link = link
        self.time = time
        self.score = score


reddit = praw.Reddit(client_id="sxEXpG454pqrpg",
                     client_secret="7wGdXpw_UK9N7ZLR11yJkwNvyzk", user_agent="Notification Center")

# returns title of submission (sub = String: subreddit name)


def get_title(sub, limit):
    content = []

    for submission in reddit.subreddit(sub).hot(limit=limit):

        content.append(str(submission.title))
    return content


# FIXME
def get_sub_image(subs):

    for sub in subs:
        print("https://www.reddit.com/r/" + sub + "/")
        url = "https://www.reddit.com/r/" + sub + "/"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
        r = requests.get(url, headers=headers)
        print(r.text)

        '''
		fp = urllib.request.urlopen("https://www.reddit.com/r/" + sub + "/")

		mybytes = fp.read()

		html = mybytes.decode("utf8")
		
		fp.close()

		soup = bs(html, 'lxml')
		#links = [item['image-file'] for item in soup.select('#Subreddit Icon [image-file]')]
		'''

    return None


def get_url(sub, limit):
    content = []

    for submission in reddit.subreddit(sub).hot(limit=limit):
        content.append('https://www.reddit.com/' + str(submission.permalink))
    return content


def get_author(sub, limit):
    content = []

    for submission in reddit.subreddit(sub).hot(limit=limit):
        content.append(str(submission.author))
    return content


def get_score(sub, limit):
    content = []

    for submission in reddit.subreddit(sub).hot(limit=limit):
        content.append(str(submission.score))
    return content


def get_time(sub, limit):
    content = []

    for submission in reddit.subreddit(sub).hot(limit=limit):
        content.append(str(datetime.utcfromtimestamp(
            submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')))

    return content


def get_info(sub, limit):
    try:
        posts = []

        content = [get_title(sub, limit), get_author(sub, limit), get_url(
            sub, limit), get_score(sub, limit), get_time(sub, limit)]

        for i in range(len(content)):
            posts.append(Post(content[0][i], content[1][i],
                              content[2][i], content[3][i], content[4][i],))

        return posts
    except:
        print('ERROR: the subreddit you are trying to access may not exist')
