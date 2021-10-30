from rss_parser.command_line_parser import CommandLineParser
from rss_parser.controller import Controller
import logging


def main():
    # parse command line arguments
    args = CommandLineParser.parse_args()

    # config logging of utility
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.WARNING)
    logger = logging.getLogger()

    # describe using arguments
    logger.debug(' '.join([f'{arg}={val}' for arg, val in vars(args).items()]))

    # execute operation using command line arguments
    Controller.execute(args)


if __name__ == "__main__":
    main()
