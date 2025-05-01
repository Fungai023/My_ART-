import requests
from bs4 import BeautifulSoup
import pandas as pd

Current_page = 1
url = f"https://books.toscrape.com/index.html"
another_url = f"https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"
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
    return book_types


def counter(book_types):
    structure = "index"  
    for index in range(1,len(book_types)-1):
        another_url = f"https://books.toscrape.com/catalogue/category/books/{book_types[index]}/{structure}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text , "html.parser")
        results =int(soup.find(class_="form-horizontal").text.strip().split(" ")[0])
        pg_count = results // 20
        if results%20 != 0 :
            final = pg_count +1

        
        if pg_count>1:
            num =2
            structure = f"page-{num}"
            if num < pg_count:
                num+=1
        
        d = preparing_(book_types[index])
    print(d)

book_types = nav_list_handler(soup)
print(book_types)
counter(book_types)

    

def product_description(book):
    response = requests.get(book)
    b_soup = BeautifulSoup(response.text, "html.parser")
    print(b_soup.find("p"))


def preparing_(genre):
    all_book = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    book_details = []
    data = {}

    for book in all_book:
        # print(book_data.text.strip())
        book_name = book.find("img").attrs["alt"]
        book_price = book.find("p",class_="price_color").text[2:]
        stock = book.find("p",class_= "instock availability").text.strip()
        book_url = book.find("a").attrs["href"]#try pulling a url reader to get product discription
        # print(f"https://books.toscrape.com/catalogue/{book_url}")
        # book_description = product_description(f"https://books.toscrape.com/catalogue/{book_url}")
        book_details.append(book_name)
        book_details.append(book_price)
        book_details.append(stock)
        book_details.append(book_url)

        data[genre] = book_details
    return data
    
    





