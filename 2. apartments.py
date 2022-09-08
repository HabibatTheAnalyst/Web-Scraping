from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

prettylist = []

def getPretty(tag, page):
    url = f'https://www.prettylittlething.com/clothing/dresses/{tag}.html?id=357&page={page}&ajax=0'
    source = requests.get(url, headers = headers)
    soup = BeautifulSoup(source.text, 'lxml')
    dress = soup.find_all('div', class_ = 'category-product')
    for item in dress:
        tag = tag
        title = item.find('h2', class_ = 'product-title').text.strip()
        price = item.find('span', class_ = 'price').text.strip()
        link = item.find('a', class_ = 'product-url')['href']

        pretty = {'tag': tag, 'title': title, 'price': price, 'link': link}
        prettylist.append(pretty)
    return

for x in range(1,3):
    getPretty('denim-dresses', x)
    getPretty('mini-dresses', x)
    
df = pd.DataFrame(prettylist)
df.to_excel('PrettyLittleThings.xlsx')
print('Finish')