import unittest

from src.web_scrapper import WebScrapper
from src.parser import parse_quote

URL_QUOTE_OF_THE_DAY = "https://www.brainyquote.com/quote_of_the_day"


class TestWebScrapper(unittest.TestCase):
    def setUp(self):
        self.scrapper = WebScrapper(URL_QUOTE_OF_THE_DAY)
        self.scrapper.load_page()

    def test_LoadPageProperly(self):
        self.assertTrue(self.scrapper.is_page_loaded(), "PageIsLoaded")

    def test_FindDailyQuote(self):
        self.assertIsNotNone(self.scrapper.find_quote_of_the_day(), "FindDailyQuote")

    def test_ParseQuote(self):
        quote_text, author = parse_quote(self.scrapper.find_quote_of_the_day())
        self.assertIsNotNone(quote_text)
        self.assertIsNotNone(author)


if __name__ == '__main__':
    unittest.main()
