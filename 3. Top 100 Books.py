import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

booklist = []

url = 'https://www.gutenberg.org/browse/scores/top'
source = requests.get(url, headers = headers)
soup = BeautifulSoup(source.text, 'html.parser')
books = soup.find('ol').find_all('li')

for book in books:
    title = book.find('a').text

    list = {'title': title}
    booklist.append(list)

time.sleep(5)
df = pd.DataFrame(booklist)
print(df)


''''
for book in books:
    title = book.find('li').a.text
    
    print(title)


EXPLORE AFRICA

        
        #price = item.find('span', class_ = 'price').text.strip()
        #link = item.find('a', class_ = 'product-url')['href']

'''