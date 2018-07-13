from bs4 import BeautifulSoup
import requests

url = "https://noticias.r7.com/sao-paulo/socos-pontapes-e-assedio-como-professores-enfrentam-a-violencia-06072018"
request = requests.get(url)

soup = BeautifulSoup(request.content, 'lxml')

articles = soup.find_all("article", {"class", "content"})

for article in articles:
    print(article.find_all("p")[0].text)
