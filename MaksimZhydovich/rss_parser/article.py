
class Article:

    def __init__(self, title, link, pub_date):
        self.__title = title
        self.__link = link
        self.__pub_date = pub_date

    def __str__(self):
        return f"Title: {self.get_title()}\nDate: {self.get_pub_date()}\nLink: {self.get_link()}"

    def get_title(self):
        return self.__title

    def get_link(self):
        return self.__link

    def get_pub_date(self):
        return self.__pub_date
