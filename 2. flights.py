from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
url = 'https://www.youtube.com/c/JohnWatsonRooney/videos'
source = session.get(url)
soup = BeautifulSoup(source.text, 'lxml')
videos = soup.find('div', class_ = 'style-scope ytd-grid-renderer')

for video in videos:

    name = video.find('h3', class_ = 'style-scope ytd-grid-renderer').a.text
    print(name)

    