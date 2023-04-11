# -*- coding: utf-8 -*-

# Необходимо было написать скрипт,
# который отслеживал бы внешний ip-адрес и в случае не того адреса,
# перезагружал бы wi-fi адаптер.

import subprocess
import logging
import datetime
from tkinter import *
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


        def clicked():  # создание всплывающего окна: "clicked" - кнопка "ОК".
            window.destroy()


        window = Tk()  # создание всплывающего окна
        window.title("Внимание!")
        window.geometry('480x200')
        lbl = Label(window, text="Внимание! IP - адрес был изменен.\n "
                                 "Необходима перезагрузка Wi-Fi.\n"
                                 "Нажмите 'ОК' для продолжения \n", fg="red",
                    font=("Arial Bold", 20))
        lbl.grid(column=0, row=0)
        btn = Button(window, text="ОК!", command=clicked, font=("Arial Bold", 15))
        btn.grid(column=0, row=1)
        window.mainloop()

        wifi = subprocess.call('netsh wlan connect name="MobileCitySouth"')  # подключение к сети WIFI
        time.sleep(5)
        if wifi == 0:
            logging.info('Wi-Fi отключен.Включение...')
            print('Wi-Fi включается...')


            def clicked2():  # создание всплывающего окна: "clicked2" - кнопка "ОК".
                window.destroy()


            window = Tk()  # создание всплывающего окна
            window.title("Внимание!")
            window.geometry('420x155')
            lbl = Label(window, text="Можно продолжать работать.\n"
                                     "Нажмите 'ОК' для продолжения\n ", fg="red",
                        font=("Arial Bold", 20))
            lbl.grid(column=0, row=0)
            btn = Button(window, text="ОК!", command=clicked2, font=("Arial Bold", 15))
            btn.grid(column=0, row=1)
            window.mainloop()
            time.sleep(5)
