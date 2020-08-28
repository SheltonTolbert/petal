from requests import get
from bs4 import BeautifulSoup


class Article():
    def __init__(self, title, description, author, link, date, read_time, category):
        self.title = title
        self.description = description
        self.author = author
        self.link = link
        self.date = date
        self.read_time = read_time
        self.category = category


def get_articles(sub):

    articles = []
    url = ('https://medium.com/topic/' + sub)
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    type(soup)
    article_containers = soup.find_all('section')

    for i in range(len(article_containers)):
        try:
            link_to_article = article_containers[i].div.section.find_all(
                'div')[16].find('a', href=True).get('href')

            article_title = article_containers[i].div.section.find_all('div')[
                0].find('a').text

            article_description = article_containers[i].div.section.find_all('div')[
                3].text

            author = article_containers[i].div.section.find_all('div')[
                8].text.split('in')[0]

            category = article_containers[i].div.section.find_all('div')[
                8].text.split('in')[1]

            date = article_containers[i].div.section.find_all('div')[
                9].text.split('·')[0]

            read_time = article_containers[i].div.section.find_all('div')[
                9].text.split('·')[1]

            articles.append(Article(article_title, article_description,
                                    author, link_to_article, date, read_time, category))

        except:
            pass

    return articles
