#This example is based of the story of Alice in Wonderland , we will be using for all the examples

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup_object = BeautifulSoup(html_doc,"lxml")
# print(soup_object.prettify())


"""
Here we use the BeautifulSoup object to read html content 
Here we make use basic understand of html to easly navigate
and maniulate this data or to search for what we need
"""
print(soup_object.title)
print(soup_object.title.name)
print(soup_object.title.parent.name)
print(soup_object.find_all("a")) #returns a list of all the anchors found 
print("\n",soup_object.p.b.text)
print(soup_object.p)
print(soup_object.find(id="link3").text,"\n")


#Here we are introduced to a deeper manipulation of this data
for link in soup_object.find_all("a"):
    print(link.get("href")) #allows use to get the link address by introducing get methods

print()
"""
We use built in get_text() methond , it needs to be invoked 
Retrieves all the text format and print
"""
print(soup_object.get_text())


