import requests
from bs4 import BeautifulSoup

for x in range(1,19):
    url = 'https://www.pararius.com/apartments/amsterdam?ac='
    source = requests.get(url + str(x))
    soup = BeautifulSoup(source.text, 'lxml')
    apartments = soup.find('ul', class_ = 'search-list').find_all('section')
        
    for apartment in apartments:
        name = apartment.find('a', class_ = 'listing-search-item__link--title').text
        price = apartment.find('div', class_ = 'listing-search-item__price').text
        location = apartment.find('div', class_ = 'listing-search-item__sub-title').text
        area = apartment.find('li', class_ = 'illustrated-features__item--surface-area').text
        rooms = apartment.find('li', class_ = 'illustrated-features__item--number-of-rooms').text

print(name, price, location, area, rooms)