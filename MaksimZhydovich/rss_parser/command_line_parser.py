import argparse
import datetime


class CommandLineParser:

    @staticmethod
    def parse_args():

        def verify_date(date):
            """
            Verifies date
            """
            return datetime.datetime.strptime(date, "%Y%m%d").date()

        parser = argparse.ArgumentParser(prog="rss_reader.py", description="Pure Python command-line RSS reader.")

        parser.add_argument("source", nargs="?", type=str, help="RSS URL")

        parser.add_argument("--version", action="version", version="Version 1.1", help="Print version info")
        parser.add_argument("--json", action="store_true", help="Print result as JSON in stdout")
        parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages")
        parser.add_argument("--limit", help="Limit news topics if this parameter provided")
        parser.add_argument('--date', type=verify_date, help="Set data")

        return parser.parse_args()
