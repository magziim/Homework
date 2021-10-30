
class Article:
    """Class provides object for <item> from RSS"""

    def __init__(self, title, link, pub_date):
        """Initialize Article with title, link and date of publication"""
        self.__title = title
        self.__link = link
        self.__pub_date = pub_date

    def __str__(self):
        """Return string representation of article"""
        return f"Title: {self.get_title()}\nDate: {self.get_pub_date()}\nLink: {self.get_link()}"

    def get_title(self):
        """Get title of article"""
        return self.__title

    def get_link(self):
        """Get link to the article"""
        return self.__link

    def get_pub_date(self):
        """Get date of publication"""
        return self.__pub_date
