from bs4 import BeautifulSoup
from bs4.element import Tag, ResultSet
import requests


# titles = soup.find_all('div', class_='m_title')
# soup.find(tag, attribute) -> Tag
# soup.find_all(tag, attribute) -> ResultSet[Tag, Tag, Tag...]
# durations = soup.find_all('div', class_='m_time')
# countries = soup.find_all('div', class_='m_data')

URL = "http://www.manascinema.com/movies" # сохраняем ссылку для парсинга 

html = requests.get(URL) # запрашиваем ответ от сайта
if html.status_code != 200: # 200 - код успешного запроса, если не 200 - останавливаем код
    raise Exception('Сайт сломался')
html_code = html.text # вытаскиваем html-код из ответа
soup = BeautifulSoup(html_code, 'html.parser') # создаем суп для фильтрации html
movie_cards = soup.find_all('div', class_='short_movie_info') # находим все карточки с фильмами. на выходе получаем список из карточек
result = [] # пустой список для сбора конечного результата
for card in movie_cards: # обращаемся к каждой карточке из списка
    try:
        duration = card.find('div', class_='m_time').getText(strip=True) # достаем из карточки продолжительность
    except AttributeError:
        duration = 'Продолжительность не указана'
    film = { # создали словарь для хранения данных
        'title': card.find('div', class_='m_title').text.strip(), # название фильма
        'duration': duration,
        'image_link': card.find('div', class_='m_thumb').find('img').get('src'), # ссылку на картинку
        'country': card.find('div', class_='m_data').getText(strip=True).replace('\r', ''), # страну производства
    }
    result.append(film) # добавляем словарь в список result


def write_to_csv(data: list):
    """ Функция для записи конечного результата в csv """
    import csv
    with open('movies.csv', 'w') as file:
        fieldnames = ['title', 'duration', 'image_link', 'country']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

write_to_csv(result)

