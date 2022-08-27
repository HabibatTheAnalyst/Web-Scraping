from bs4 import BeautifulSoup
import requests, openpyxl # to open the scrapped data in excel


url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')
<<<<<<< HEAD
movies = soup.find('tbody', class_ = 'lister-list').find_all('tr')
=======
movies = soup.find('tbody', class_ = 'lister-list').find_all('tr')
>>>>>>> 6e69f629d17150e030166953cbf001256825fbe9
