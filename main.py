import requests
from bs4 import BeautifulSoup

#variável para guardar endereço de um site
response = requests.get('https://quotes.toscrape.com/')

#variável para usar o beautifulsoup 
soup = BeautifulSoup(response.text, 'html.parser')

#variável que pega o texto do site
frases = soup.find_all('span', class_='text')

#exibir texto
for frase in frases:
    print(frase.text)


#py main.py