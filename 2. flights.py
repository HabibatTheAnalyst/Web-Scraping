from bs4 import BeautifulSoup
import requests, openpyxl # to open the scrapped data in excel


url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')
movies = soup.find('tbody', class_ = 'lister-list').find_all('tr')
