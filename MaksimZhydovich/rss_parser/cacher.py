from .article import Article


class Cacher:

    def __init__(self, file="articles.txt"):
        self.file = file

    def cache_articles(self, articles):
        with open(self.file, "w") as f:
            for article in articles:
                f.write(article.get_pub_date().isoformat(' ') + "\n")
                f.write(article.get_title() + "\n")
                f.write(article.get_link() + "\n")

    def get_articles_by_date(self, date):
        articles = []
        try:
            with open(self.file, "r") as f:
                lines = f.readlines()
                n = len(lines)
                for i in range(n - 2):
                    article_date = lines[i].rstrip()
                    article_title = lines[i + 1].rstrip()
                    article_link = lines[i + 2].rstrip()
                    if date == article_date[:10]:
                        articles.append(Article(article_title, article_link, article_date))
        except Exception as e:
            print(e)

        if len(articles) == 0:
            raise Exception(f"There are not news for this date: {date}")

        return articles
