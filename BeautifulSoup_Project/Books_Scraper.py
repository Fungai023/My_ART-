import requests
from bs4 import BeautifulSoup
import pandas as pd

Current_page = 1
url = f"https://books.toscrape.com/catalogue/page-{Current_page}.html"

response = requests.get(url)
soup = BeautifulSoup(response.text , "html.parser")

print(soup.prettify())