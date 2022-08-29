import requests
from bs4 import BeautifulSoup

url = 'https://www.pararius.com/apartments/amsterdam?ac=1'
source = requests.get(url)
soup = BeautifulSoup(source.text, 'html.parser')

print(soup)