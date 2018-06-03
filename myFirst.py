import requests
from bs4 import BeautifulSoup

url = "https://www.gazetadopovo.com.br/curitiba/escolas-municipais-de-curitiba-ja-foram-alvo-de-275-episodios-de-violencia-em-2018-6r7imnmxot3som8b3dkbp377e"

r = requests.get(url)

soup = BeautifulSoup(r.content)

print(soup.prettify())
