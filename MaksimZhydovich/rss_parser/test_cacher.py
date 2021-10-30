import unittest

from article import Article
from cacher import Cacher


class TestCacher(unittest.TestCase):
    """Class provides testing of cache methods"""

    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        """SetUp Cacher for testing"""
        self.cacher = Cacher("test_cache.txt")

    def test_get_by_date(self):
        """Test for --date arguments"""
        articles = [Article("Title1", "link1",  "2021-10-28"), Article("Title2", "link2",  "2021-10-28")]
        articles_from_file = self.cacher.get_articles_by_date("2021-10-28")
        self.assertEqual(articles, articles_from_file)


# Executing the tests
if __name__ == "__main__":
    unittest.main()
