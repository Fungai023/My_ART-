import requests
from bs4 import BeautifulSoup
import pandas as pd

class bookScraper():
    
    """
    Constructor that accept args , for more data processing
    """
    def __init__(self , pageCount = 1):
        data = ""
        self.page_count = pageCount
        self.url = f"https://books.toscrape.com/catalogue/category/books/{data}/page-{pageCount}.html"
        

    def url_reader(self , url):
        response = requests.get(url)
        self.scraper = BeautifulSoup(response.text , "lxml")
        

    """
    Extracts data from the 'nav nav-list' class within a <div> element.

    Reads all list items (<li>) and stores their text content in a list,
    removing unnecessary whitespace. The resulting list is intended for
    use in creating a dictionary, which will later be used to form a DataFrame.
    """
    def nav_list_handler(self):
        book_types = []
        navlist_data = self.scraper.find(class_="nav nav-list").text.strip().split("\n")
        for item in navlist_data:
            if len(item.strip()) != 0:
                book_types.append(item.strip())
        return book_types
    
