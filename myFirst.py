'''
    Using BeautifulSoup, a python library that helps up to scrape data into a website by parsing it's html, to mine data about violence in brazilian schools

    author: @jvitorfranca
'''

#Libraries we'll use
from bs4 import BeautifulSoup
import requests

#url of the page we're looking for and requesting
url = "https://noticias.r7.com/sao-paulo/socos-pontapes-e-assedio-como-professores-enfrentam-a-violencia-06072018"
request = requests.get(url)

#scraping it's content
soup = BeautifulSoup(request.content, 'lxml')

#finding some attributes of this page
articles = soup.find_all("article", {"class", "content"})

#parsing
for article in articles:
    print(article.find_all("p")[0].text)


#counting the occurencies of a specific word
text = soup.get_text()
print(text.count('escola'))
