from bs4 import BeautifulSoup
import requests


response = requests.get("https://wttr.in/")
soup = BeautifulSoup(response.text , "html.parser")

print(soup.prettify())