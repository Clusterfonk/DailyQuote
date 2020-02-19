import unittest


from src.quote import Quote


def mock_fetch_quote_text():
    return "This is a mockup quote text."


def mock_fetch_author():
    return "mockup author"


class TestQuote(unittest.TestCase):
    def setUp(self):
        self.quote = Quote()

    def test_emptyQuoteShouldBeEmpty(self):
        self.assertTrue(len(self.quote.get_text()) == 0)

    def test_emptyQuoteShouldHaveNoAuthor(self):
        self.assertTrue(self.quote.get_author() is None)

    def test_fetchQuoteOfTheDay(self):
        self.quote.get_daily_quote(fetch_text=mock_fetch_quote_text, fetch_author=mock_fetch_author)
        self.assertEqual(self.quote.get_text(), mock_fetch_quote_text())
        self.assertEqual(self.quote.get_author(), mock_fetch_author())


if __name__ == '__main__':
    unittest.main()
