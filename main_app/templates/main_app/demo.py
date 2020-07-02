from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.thisdayinmusic.com', headers={'User-Agent': 'Mozilla/5.0'}).text

soup = BeautifulSoup(source, 'html.parser')
print(soup)

artist = soup.find('tddim-born--artist')
artist = soup.find('span', {'class': 'tddim-born--artist'})
print(artist)