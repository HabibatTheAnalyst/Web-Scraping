import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

url = 'https://africanfinancials.com/nigerian-stock-exchange-share-prices/'
source = requests.get(url, headers = headers)
soup = BeautifulSoup(source.text, 'html.parser')
shares = soup.find('tbody', class_ = 'wpv-loop').find_all('tr')

# print(source)
# print(soup.title.text)
# Nigerian Stock Exchange Share Prices - AfricanFinancials

for stock in shares:
    company = stock.find('td', class_ = 'dtr-control')

print(company)