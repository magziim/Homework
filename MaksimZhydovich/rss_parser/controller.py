from .parser import Parser
from .printer import Printer
from .cacher import Cacher


class Controller:
    """Class that execute all operations with command line arguments"""

    @staticmethod
    def execute(args):
        """Execute all operations with command line arguments"""

        # create printer and cacher
        printer = Printer(args.json)
        cacher = Cacher()

        articles = []
        if args.source is not None:
            # if reader hasn't been called before we need to create parser,
            # parse and cache all articles from `source` url
            parser = Parser(args.source)
            articles = parser.parse_articles()
            cacher.cache_articles(articles)

        if args.date:
            # if we have date we should get articles from cache
            try:
                articles = cacher.get_articles_by_date(args.date.strftime("%Y-%m-%d"))
            except Exception as e:
                print(e)

        if args.to_pdf:
            # convert to .pdf
            cacher.cache_articles_in_pdf()

        if args.to_html:
            # convert to .html
            cacher.cache_articles_in_html()

        # print articles
        if args.limit:
            printer.print(articles[:int(args.limit)])
        else:
            printer.print(articles)
