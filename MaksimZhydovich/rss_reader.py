from rss_parser.command_line_parser import CommandLineParser
from rss_parser.controller import Controller
import logging


def main():
    args = CommandLineParser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.WARNING)
    logger = logging.getLogger()
    logger.debug(' '.join([f'{k}={v}' for k, v in vars(args).items()]))
    Controller.manipulate(args)


if __name__ == "__main__":
    main()
