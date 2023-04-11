# -*- coding: utf-8 -*-

# то же самое, что и v1.3, но без графического интерфейса

import subprocess
import logging
import datetime
from requests import get
import time

now = datetime.datetime.now()  # лог-файл
logging.basicConfig(filename='app.log', level=logging.INFO, filemode='a',
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning(f'Начало работы.Время : {now.strftime("%Y-%m-%d-%H.%M")}')

running = True
while running:  # проверка IP
    ip = get('http://108.171.202.203').text  # Запрос на 108.171.202.203 для получения IP
    print('Внешний IP адрес: {}'.format(ip))
    if ip == "your_ip":
        print('ok')
        logging.info(
            f'Проверка IP завершена успешно, внешний IP адрес :{ip}.Время завершения: {now.strftime("%Y-%m-%d-%H.%M")}')
        time.sleep(10)
    else:
        print('not ok')
        logging.info(
            f'Проверка IP показала - внешний IP адрес :{ip}, неверный.Время ошибки: {now.strftime("%Y-%m-%d-%H.%M")}')

        wifi = subprocess.call('netsh wlan connect name="MobileCitySouth"')  # подключение к сети WIFI
        time.sleep(5)
        if wifi == 0:
            logging.info('Wi-Fi отключен.Включение...')
            print('Wi-Fi включается...')
            time.sleep(5)
