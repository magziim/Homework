from .parser import Parser
from .printer import Printer
from .cacher import Cacher


class Controller:

    @staticmethod
    def manipulate(args):
        printer = Printer(args.json)
        cacher = Cacher()

        articles = []
        if args.source is not None:
            parser = Parser(args.source)
            articles = parser.parse_articles()
            cacher.cache_articles(articles)

        if args.date:
            try:
                articles = cacher.get_articles_by_date(args.date.strftime("%Y-%m-%d"))
            except Exception as e:
                print(e)

        printer.print(articles[:int(args.limit)])
