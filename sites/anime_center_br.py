import requests
from bs4 import BeautifulSoup


def anime_center_br_scrapping(url):
     headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
     }

     response = requests.get(url, headers=headers)
     print(response.status_code)

     soup = BeautifulSoup(response.content, 'html.parser')
     soup_find = soup.find('div', class_='post-text-content my-3')
     capitulo_nome = soup_find.find_all('h3')
     capitulo_conteudo = soup_find.find_all('p')

