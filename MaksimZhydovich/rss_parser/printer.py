import json


class Printer:

    def __init__(self, is_json):
        self.__is_json = is_json

    def print(self, news):
        if self.__is_json:
            for article in news:
                print(json.dumps({
                    "Title": article.get_title(),
                    "Date": article.get_pub_date(),
                    "Link": article.get_link()
                }))
                print("\n")
        else:
            for article in news:
                print(article)
                print("\n")
