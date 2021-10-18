import logging
from time import time, sleep
from contextlib import ContextDecorator


class Loger(ContextDecorator):
    """Decorator with context manager support for writing execution time to log-file"""

    def __init__(self, file_name):
        logging.basicConfig(level=logging.INFO, filename=file_name, filemode='w')
        print("init")

    def __enter__(self):
        self.start_time = time()
        logging.info(f"Start: {self.start_time}")
        print("enter")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end_time = time()
        logging.info(f"Stop: {self.end_time}")
        logging.info(f"{self.end_time - self.start_time} seconds elapsed")
        print("exit")


@Loger("output.txt")
def timed():
    print("timed start")
    sleep(5)
    print("timed stop")


def main():
    timed()


if __name__ == "__main__":
    main()
