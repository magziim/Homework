from .parser import Parser
from .printer import Printer


class Controller:

    @staticmethod
    def manipulate(args):
        parser = Parser(args.source)
        printer = Printer(args.json)

        printer.print(parser.parse_news()[:int(args.limit)])