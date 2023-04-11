# парсер на охотничий магазин, с выводом по охотничьему оружию

import requests
from bs4 import BeautifulSoup

url = 'https://gunsbroker.ru/search//none/&cat=hunting&subcat=1&cal=0&reloading_type=11&stvol_type=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('section', class_='main__item--desc')

for n, i in enumerate(items, start=1):
    itemName = i.find('h3').text
    itemPrice = i.find('strong').text
    itemPlace = i.find('address').text
    itemTime = i.find('span').text
    print(f'{n}:  {itemName} за {itemPrice} Адрес {itemPlace}, дата публикации: {itemTime}')
