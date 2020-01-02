from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame
import csv

headers = {
    'email: pxie2001@gmail.com'
}
#scrapes 2019 Total Player stats from bball-ref

url='https://www.basketball-reference.com/leagues/NBA_2019_totals.html'.format(2019)

html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')

#table headers
headers = ['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

#avoiding first row
rows = soup.findAll('tr')[1:]
stats = [[td.getText() for td in rows[i].findAll('td')]
        for i in range(len(rows))]

playerstats = DataFrame(stats,columns=headers)

nbaplayerstats2019 = playerstats.to_csv(r'D:\Webscrape\nbaplayerstats2019.csv')