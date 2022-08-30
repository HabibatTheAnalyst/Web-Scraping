import requests
from bs4 import BeautifulSoup

for x in range(1,19):
    url = 'https://www.pararius.com/apartments/amsterdam/page-2/sort-price-low'
    source = requests.get(url) # + str(x))
    soup = BeautifulSoup(source.text, 'lxml')
    apartments = soup.find('ul', class_ = 'search-list').find_all('section')

    for apartment in apartments:
        name = apartment.find('h2', class_ = 'listing-search-item__title').a.text.replace(' ', '')
        price = apartment.find('div', class_ = 'listing-search-item__price').text.replace(' ','')
        location = apartment.find('div', class_ = 'listing-search-item__sub-title').text.replace(' ', '')
        area = apartment.find('li', class_ = 'illustrated-features__item--surface-area').text.replace(' ', '')
        rooms = apartment.find('li', class_ = 'illustrated-features__item--number-of-rooms').text.replace(' ', '')
        link = apartment.h2.a['href']

        print({name}, {price}, {location}, {area}, {rooms}, {link})