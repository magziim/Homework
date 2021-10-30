import json


class Printer:
    """Class provides printing articles to console"""

    def __init__(self, is_json):
        """Initialize class with format of output"""
        self.__is_json = is_json

    def print(self, news):
        """Print articles to console"""
        if self.__is_json:
            for article in news:
                print(json.dumps({
                    "Title": article.get_title(),
                    "Date": article.get_pub_date().isoformat(" "),
                    "Link": article.get_link()
                }))
                print("\n")
        else:
            for article in news:
                print(article)
                print("\n")
