
class Pagination:
    """Class provides arrange text on pages"""

    def __init__(self, text, count):
        """Init Pagination class"""
        self.text = text
        self.count = count

    def page_count(self):
        """Return count of pages"""
        return len(self.text) // self.count + 1

    def item_count(self):
        """Return count of symbols in text"""
        return len(self.text)

    def count_items_on_page(self, page):
        """Return count of symbols on page"""
        if page >= self.page_count():
            raise Exception("Invalid index. Page is missing")
        return len(self.text[page * self.count:(page + 1) * self.count])

    def find_page(self, word):
        """Return pages which contain `word`"""
        pages = []
        for i in range(len(self.text)):
            if self.text.startswith(word, i):
                for q in range(i // self.count, (i + len(word)) // self.count + 1):
                    pages.append(q)

        if not pages:
            raise Exception(f"{word} is missing on the pages")

        return pages

    def display_page(self, page):
        """Return page"""
        if page >= self.page_count():
            raise Exception("Invalid index. Page is missing")
        return self.text[page * self.count:(page + 1) * self.count]


def main():
    pages = Pagination("Your beautiful text", 5)
    print(pages.page_count())
    print(pages.item_count())

    print(pages.count_items_on_page(0))
    print(pages.count_items_on_page(1))
    print(pages.count_items_on_page(2))
    print(pages.count_items_on_page(3))
    # print(pages.count_items_on_page(4))

    print(pages.find_page("e"))
    print(pages.find_page("Your"))
    print(pages.find_page("beautiful"))
    # print(pages.find_page("great"))

    print(pages.display_page(0))
    print(pages.display_page(1))
    print(pages.display_page(2))
    print(pages.display_page(3))
    # print(pages.display_page(4))


if __name__ == "__main__":
    main()
