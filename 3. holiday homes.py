import requests
from bs4 import BeautifulSoup

for x in range(1,10):
    url = 'https://www.brittany-ferries.co.uk/holidays/search?vt=0&s=ASC&p='
    source = requests.get(url + str(x))
    soup = BeautifulSoup(source.text, 'lxml')
    homes = soup.find('div', class_ = 'product-grid grid').find_all('dd-product-card')

    for home in homes:
        name = home.h3.h2.text