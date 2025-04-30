import requests
from bs4 import BeautifulSoup
import pandas as pd

Current_page = 1
url = f"https://books.toscrape.com/catalogue/page-{Current_page}.html"

response = requests.get(url)
soup = BeautifulSoup(response.text , "html.parser")

"""
Handles the data from the nav nav list class stored in the div
Reads all list items and puts them in a list after removing unnessecary extra spaces
Data to be used during the creating of a dictionary , to be required to form a data frame 
"""
def nav_list_handler(soup):
    book_types = []
    navlist_data = soup.find(class_="nav nav-list").text.strip().split("\n")
    for item in navlist_data:
        if len(item.strip()) != 0:
            book_types.append(item.strip())

book_types = nav_list_handler(soup)



all_book = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
book_details = []
for book in all_book:
        # print(book_data.text.strip())
        book_name = book.find("img").attrs["alt"]
        book_price = book.find("p",class_="price_color").text[2:]
        book_about = book.find("a").attrs["href"] #try pulling a url reader to get product discription
        print(book_about)




