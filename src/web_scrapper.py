import requests

from bs4 import BeautifulSoup


class WebScrapper:
    def __init__(self, url):
        self.__url = url
        self.__page = None

    def load_page(self):
        self.__page = requests.get(self.__url)

    def is_page_loaded(self):
        return int(self.__page.status_code / 100) == 2

    def find_quote_of_the_day(self):
        page_parse_tree = BeautifulSoup(self.__page.text, 'html.parser')
        return page_parse_tree.find(title="view quote").next_element['alt']
