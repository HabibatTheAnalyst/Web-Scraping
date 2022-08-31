import requests
from bs4 import BeautifulSoup

#for x in range(1,30):
url = 'https://www.brittany-ferries.co.uk/holidays/search?vt=0&s=ASC&p='
source = requests.get(url) # + str(x))
soup = BeautifulSoup(source.text, 'lxml')
homes = soup.find('section', class_ = 'ng-star-inserted').find_all('dd-product-card')

print(len(homes))
'''
for home in homes:
    name = home.find('_ngcontent-serverapp-c290', class_ = 'ng-star-inserted')
    print(name)
'''