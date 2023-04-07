from bs4 import BeautifulSoup
from bs4.element import Tag, ResultSet
import requests


URL = "http://www.manascinema.com/movies"

html = requests.get(URL)
if html.status_code != 200:
    raise Exception('Сайт сломался')

html_code = html.text
# print(html_code)
soup = BeautifulSoup(html_code, 'html.parser')
# titles = soup.find_all('div', class_='m_title')
# soup.find(tag, attribute) -> Tag
# soup.find_all(tag, attribute) -> ResultSet[Tag, Tag, Tag...]
# durations = soup.find_all('div', class_='m_time')
# countries = soup.find_all('div', class_='m_data')
movie_cards = soup.find_all('div', class_='short_movie_info')
result = []
card: Tag
for card in movie_cards:
    try:
        duration = card.find('div', class_='m_time').getText(strip=True)
    except AttributeError:
        duration = 'Продолжительность не указана'
    film = {
        'title': card.find('div', class_='m_title').text.strip(),
        'duration': duration,
        'image_link': card.find('div', class_='m_thumb').find('img').get('src'),
        'country': card.find('div', class_='m_data').getText(strip=True).replace('\r', ''),
    }
    result.append(film)
# print(result)

def write_to_csv(data: list):
    import csv
    with open('movies.csv', 'w') as file:
        fieldnames = ['title', 'duration', 'image_link', 'country']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

write_to_csv(result)

