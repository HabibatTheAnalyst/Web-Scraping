from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

prettylist = []

def getPretty(tag, page):
    url = f'https://www.prettylittlething.com/clothing/dresses/{tag}.html?id=357&page={page}&ajax=0'
    source = requests.get(url, headers = headers)
    soup = BeautifulSoup(source.text, 'lxml')
    dress = soup.find_all('div', class_ = 'category-product')
    for item in dress:
        tag = tag
        name = item.find('h2', class_ = 'product-title').text.strip()
        price = item.find('span', class_ = 'price').text.strip()
        link = item.find('a', class_ = 'product-url')['href']

        pretty = {'tag': tag, 'name': name, 'price': price, 'link': link}
        prettylist.append(pretty)
    return

for x in range(1,54):
    getPretty('denim-dresses', x)
    getPretty('mini-dresses', x)
time.sleep(5)

df = pd.DataFrame(prettylist)
df.to_excel('PrettyLittleThings.xlsx', index = False)
print('Finish')