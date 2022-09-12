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

<<<<<<< HEAD
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
=======
<<<<<<<< HEAD:3. holiday homes.py
time.sleep(5)
df = pd.DataFrame(booklist)
df.to_excel('Top 100 Books', index = False)
print('Finish')
========


        
        #price = item.find('span', class_ = 'price').text.strip()
        #link = item.find('a', class_ = 'product-url')['href']
>>>>>>>> 001893d5f2038858faf344b92fd3cd37ca99e045:3. Top 100 Books.py
>>>>>>> 001893d5f2038858faf344b92fd3cd37ca99e045
