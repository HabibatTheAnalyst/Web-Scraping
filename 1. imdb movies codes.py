from csv import excel
from os import readlink
from bs4 import BeautifulSoup
import requests, openpyxl # to open the scrapped data in excel

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Rated Movies'
sheet.append(['rank', 'name', 'year', 'rating'])

# print(excel.sheetnames) -- to print the sheet name

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')
movies = soup.find('tbody', class_ = 'lister-list').find_all('tr')

# print(len(movies)) -- to find the total number of the movies

for movie in movies:

    name = movie.find('td', class_ = 'titleColumn').a.text # allows the code to return only the content contained in the tag 'a'
    rank = movie.find('td', class_ = 'titleColumn').get_text(strip = True).split('.')[0]
    year = movie.find('td', class_ = 'titleColumn').span.text.strip('()') # strip to remove the parenthesis
    rating = movie.find('td', class_ = 'ratingColumn imdbRating').strong.text

    print(rank, name, year, rating)
    sheet.append([rank, name, year, rating])

excel.save('IMDB Movie Ratings.xlsx')