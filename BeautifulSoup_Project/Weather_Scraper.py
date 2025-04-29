from bs4 import BeautifulSoup
import requests


response = requests.get("https://wttr.in/")
soup = BeautifulSoup(response.text , "html.parser")

my_data = soup.span
print(my_data)
