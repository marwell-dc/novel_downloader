import requests
from bs4 import BeautifulSoup
import json

url = 'https://topnovelupdates.com/book/god-of-blackfield/'


def get_metadata():
     data = {}
     response = requests.get(url)
     print(response.status_code)
     html = BeautifulSoup(response.content, 'html.parser')
     name = html.find('h1', class_='novel-title text2row')
     author = html.find('div', class_='author')
     print(author)
     print(name.text)
     quit()


def top_novel_updates_scrapping(url):
     response = requests.get(url)
     html = BeautifulSoup(response.content, 'html.parser')
     html_caption = html.find('div', id='content')
     caption = html_caption.find_all('p', class_='')
     caption.insert(0, html_caption.find('h4'))
     return caption

