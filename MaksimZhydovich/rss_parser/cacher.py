from .article import Article
from fpdf import FPDF


class Cacher:
    """Class provides caching articles to file"""

    def __init__(self, file="articles.txt"):
        """Initialize class with file to write articles"""
        self.__file = file

    def cache_articles(self, articles):
        """Cache articles to file .txt"""
        with open(self.__file, "w", encoding='utf-8') as f:
            for article in articles:
                f.write(article.get_pub_date().isoformat(' ') + "\n")
                f.write(article.get_title() + "\n")
                f.write(article.get_link() + "\n")

    def cache_articles_in_pdf(self):
        """Convert file with articles to .pdf"""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        with open(self.__file, "r", encoding='utf-8') as f:
            for line in f:
                try:
                    pdf.cell(50, 5, txt=line, align='C')
                    pdf.cell()
                except Exception as e:
                    print(e)
        pdf.output("articles.pdf", "F")

    def cache_articles_in_html(self):
        """Convert file with articles to .html"""
        with open(self.__file, "r", encoding='utf-8') as f:
            lines = f.readlines()

        with open("articles.html", "w", encoding="utf-8") as f:
            i = 0
            for line in lines:
                f.write("<pre>" + line + "</pre>")
                i += 1
                if i % 3 == 0:
                    f.write("<br>")

    def get_articles_by_date(self, date):
        """Return articles by a specific date"""
        articles = []
        try:
            with open(self.__file, "r", encoding='utf-8') as f:
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
