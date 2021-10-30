import requests
import datetime
from bs4 import BeautifulSoup

from .article import Article


class Parser:
    """Class provides parsing of articles from web-page"""

    def __init__(self, url):
        """Initialize parser with `url` - path to web-page"""
        self.__url = url

    def parse_articles(self):
        """Parse articles"""
        articles = []

        # send GET()-request
        r = requests.get(self.__url)

        # get text of page
        soup = BeautifulSoup(r.text, "xml")

        # find <channel> of articles
        channel = soup.find('channel')
        # find all <item> on the page
        news = channel.findAll('item')

        def parse_date(date):
            """Check if date format is allowed and parse it"""

            # can add new format of date
            allowed_date_formats = [
                "%a, %d %b %Y %H:%M:%S %z",
                "%a, %d %b %Y %H:%M:%S %Z",
                "%Y-%m-%dT%H:%M:%SZ",
            ]

            for date_format in allowed_date_formats:
                try:
                    return datetime.datetime.strptime(date, date_format)
                except Exception:
                    print(f"Unknown date format {date}")

        for article in news:
            article_title = article.title.string
            article_link = article.link.string
            article_pub_date = parse_date(article.pubDate.string)
            articles.append(Article(article_title, article_link, article_pub_date))

        # return list of Articles
        return articles
