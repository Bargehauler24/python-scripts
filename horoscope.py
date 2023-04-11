# парсер на гороскоп

import requests
from bs4 import BeautifulSoup


def response():
    url = 'https://retrofm.ru'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')

    object_zodiac = ['index_zodiac_1', 'index_zodiac_2', 'index_zodiac_3',
                     'index_zodiac_4', 'index_zodiac_5', 'index_zodiac_6',
                     'index_zodiac_7', 'index_zodiac_8', 'index_zodiac_9',
                     'index_zodiac_10', 'index_zodiac_11', 'index_zodiac_12']

    for i in object_zodiac:
        index_zodiac = soup.find("div", id=f'{i}').text
        print(index_zodiac)


if __name__ == '__main__':
    response()
