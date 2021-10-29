import requests
import datetime
from bs4 import BeautifulSoup

from .article import Article


class Parser:

    def __init__(self, url):
        self.url = url

    def parse_articles(self):
        articles = []

        # send GET()-request
        r = requests.get(self.url)

        # get .html
        soup = BeautifulSoup(r.text, "xml")

        channel = soup.find('channel')
        news = channel.findAll('item')

        def parse_date(date):
            # can add new format of date
            for fmt in ["%Y-%m-%dT%H:%M:%SZ", "%a, %d %m %Y %H:%M:%S %Z"]:
                try:
                    return datetime.datetime.strptime(date, fmt)
                except Exception:
                    print(f"Unknown date format {date}")

        for article in news:
            article_title = article.title.string
            article_link = article.link.string
            article_pub_date = parse_date(article.pubDate.string)
            articles.append(Article(article_title, article_link, article_pub_date))

        return articles
