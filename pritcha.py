# задача состояла в том, чтобы написать парсер на
# православный сайт и отправлять притчу дня в группу в telegram

import requests
from bs4 import BeautifulSoup
# import telebot


def response():
    url = 'https://azbyka.ru/days/'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    pritch = soup.find("div", id="pritcha").text
    print(pritch)
    # token = 'telegram token'
    # bot = telebot.TeleBot(token)
    # chat_id = 'chat id telegram'
    # text = pritch
    # bot.send_message(chat_id, text)


if __name__ == '__main__':
    response()
