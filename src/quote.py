class Quote:
    def __init__(self):
        self.__author = None
        self.__text = None

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_daily_quote(self, fetch_text, fetch_author):
        self.__text = fetch_text()
        self.__author = fetch_author()

