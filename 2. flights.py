from bs4 import BeautifulSoup
import requests


url = 'https://www.expedia.com/Flights-Search?d1=2022-12-22&d2=2023-01-05&flight-type=on&fromDate=12%2F22%2F2022&leg1=from%3ALondon%20%28LON%20-%20All%20Airports%29%2Cto%3ALagos%20%28LOS%20-%20Murtala%20Muhammed%20Intl.%29%2Cdeparture%3A12%2F22%2F2022TANYT&leg2=from%3ALagos%20%28LOS%20-%20Murtala%20Muhammed%20Intl.%29%2Cto%3ALondon%20%28LON%20-%20All%20Airports%29%2Cdeparture%3A1%2F5%2F2023TANYT&mode=search&options=cabinclass%3Aeconomy&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY&toDate=1%2F5%2F2023&trip=roundtrip'
source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')
flights = soup.find('ul', class_ = 'uitk-typelist uitk-typelist-orientation-stacked uitk-typelist-size-2 uitk-typelist-spacing').find_all('li')

for flight in flights:

    name = flight.find('div', class_ = 'uitk-layout-grid-item uitk-layout-grid-item-columnspan uitk-layout-grid-item-columnspan-medium-1').div # allows the code to return only the content contained in the tag 'a'
    print(name)
