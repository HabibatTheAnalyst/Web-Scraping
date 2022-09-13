from xml.dom.minidom import Attr
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

headers = {'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

stocklist = []

url = 'https://africanfinancials.com/nigerian-stock-exchange-share-prices/'
source = requests.get(url, headers = headers)
soup = BeautifulSoup(source.text, 'html.parser')
shares = soup.find('tbody', class_ = 'wpv-loop').find_all('tr')

# print(source)
# print(soup.title.text)
# Nigerian Stock Exchange Share Prices - AfricanFinancials

for stock in shares:
    company = stock.find('td').text
    price = stock.find('td', class_ = 'numeric').text

    share = {'company':company, 'price':price}
    stocklist.append(share)

time.sleep(5)
df = pd.DataFrame(stocklist)
df.to_excel('Nigerian Stock Exchange.xlsx', index = False)
print('Finish')