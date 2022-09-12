import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

url = 'https://twitter.com/search?q=%22Irish%20Twitter%22&src=trend_click&vertical=trends'
source = requests.get(url, headers = headers)
soup = BeautifulSoup(source.text, 'lxml')
tweets = soup.find_all('div', class_ = 'css-1dbjc4n')

for tweet in tweets:
        name = tweet.find('a', class_ = 'css-4rbku5')['href']

        print(name)



        
        #price = item.find('span', class_ = 'price').text.strip()
        #link = item.find('a', class_ = 'product-url')['href']
