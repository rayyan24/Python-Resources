'''
pip install requests
pip install bs4
pip install html5lib

Steps
1 Get the HTML
2 Parse the HTML
2 Traversal the HTML as Tree
'''
import requests
from bs4 import BeautifulSoup

url="https://www.geeksforgeeks.org/getter-and-setter-in-python/"
html=requests.get(url)
htmlContent=html.content # this variable contains all the html code in text form

soup=BeautifulSoup(htmlContent,"html.parser")
# print(soup.prettify())#this variable contains all the html code in text form but with complete indentation

# get all the p tags in page
# pTags=soup.find_all('a')
# for i in pTags:
#     print(i,end="\n\n")

firstP=soup.find("p") # returns the first tag specefied
print(firstP)

