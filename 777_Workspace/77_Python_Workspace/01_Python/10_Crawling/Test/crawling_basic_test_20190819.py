import requests
from bs4 import BeautifulSoup

req = requests.get('https://finance.naver.com/item/main.nhn?code=085370')

html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select('h3 > a')
print(my_titles)