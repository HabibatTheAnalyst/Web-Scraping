<<<<<<< HEAD
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
df.to_excel('Top 100 Books.xlsx', index = False)
print('Finish')
=======

>>>>>>> b86d4cd4a3c51f476232bc83e08b9360373b9a3e
