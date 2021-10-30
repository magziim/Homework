import argparse
import datetime


class CommandLineParser:
    """Class provides parsing of command line arguments"""

    @staticmethod
    def parse_args():
        """Method for parse arguments from command line"""

        def verify_date(date):
            """Verify date"""
            return datetime.datetime.strptime(date, "%Y%m%d").date()

        # create parser
        parser = argparse.ArgumentParser(prog="rss_reader.py", description="Pure Python command-line RSS reader.")

        # add positional arguments
        parser.add_argument("source", nargs="?", type=str, help="RSS URL")

        # add optional arguments
        parser.add_argument("--version", action="version", version="Version 1.1", help="Print version info")
        parser.add_argument("--json", action="store_true", help="Print result as JSON in stdout")
        parser.add_argument("--to_pdf", action="store_true", help="Cache articles in .pdf")
        parser.add_argument("--to_html", action="store_true", help="Cache articles in .html")
        parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages")
        parser.add_argument("--limit", help="Limit news topics if this parameter provided")
        parser.add_argument('--date', type=verify_date, help="Set data")

        # return args from command line
        return parser.parse_args()
