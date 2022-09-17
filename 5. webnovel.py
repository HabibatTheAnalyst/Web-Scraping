import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

url = 'https://www.webnovel.com/search?keywords=ash_knight17'
source = requests.get(url, headers = headers)
soup = BeautifulSoup(source.text, 'lxml')
novels = soup.find('ul', class_ = 'ser-ret').find_all('li')

for novel in novels:
    title = novel.find('a', class_ = 'c_000').text
    try: # to avoid attribute error because there is an empty list
        ratings = novel.find('p', class_ = 'g_star_num').small.text
    except AttributeError:
        ratings = None
    print(ratings)
        
#print(soup.title.text)