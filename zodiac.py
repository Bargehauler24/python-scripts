# второй вариант парсера на гороскоп

import requests
from bs4 import BeautifulSoup


def response():
    url = 'https://retrofm.ru'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    items = soup.find_all('div', class_='index_horoscope_box')

    for n, i in enumerate(items, start=1):
        itemName = i.find('h4').text
        itemText = i.find('p').text
        print(f'{n}:  {itemName}  {itemText}')


if __name__ == '__main__':
    response()
