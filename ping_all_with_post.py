# -*- coding: utf-8 -*-

# пинг устройств и отправка вывода на почту

import logging
import datetime
from pythonping import ping
import smtplib  # Импортируем библиотеку по работе с SMTP
import os  # Функции для работы с операционной системой, не зависящие от используемой операционной системы

# Добавляем необходимые подклассы - MIME-типы
import mimetypes  # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders  # Импортируем энкодер
from email.mime.base import MIMEBase  # Общий тип
from email.mime.text import MIMEText  # Текст/HTML
from email.mime.image import MIMEImage  # Изображения
from email.mime.audio import MIMEAudio  # Аудио
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект

now = datetime.datetime.now()  # Создание лог-файла
filename = f'ping_all {now.strftime("%Y-%m-%d-%H.%M")}.log'
logging.basicConfig(filename=filename, level=logging.INFO, filemode='a',
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning(f'Начало работы.\n'
                f'ПРОВЕРКА АНТЕНН.\n'
                f'ВРЕМЯ : {now.strftime("%Y-%m-%d-%H.%M")}')

ip_list_ant = {
    "place 1": "address 1",
    "place 2": "address 2",
    "place 3": "address 3",
    "place 4": "address 4"
}

for key in ip_list_ant:
    if ping(ip_list_ant[key], verbose=False, count=4).success():
        print(f'Антенна {ip_list_ant[key]}  доступна!')
        logging.info(
            f'Антенна на объекте: {key}  с ip адресом : {ip_list_ant[key]} доступна.')
    else:
        print(f'Антенна {ip_list_ant[key]}  не доступна!')
        logging.info(
            f'Антенна на объекте: {key}  с ip адресом : {ip_list_ant[key]} не доступна.')

logging.warning(f'ПРОВЕРКА РЕГИСТРАТОРОВ\n'
                f'ВРЕМЯ : {now.strftime("%Y-%m-%d-%H.%M")}')

object_reg = {
    "place 1": "address 1",
    "place 2": "address 2",
    "place 3": "address 3",
    "place 4": "address 4"
}

for key in object_reg:
    if ping(object_reg[key], verbose=False, count=4).success():
        print(f'Регистратор {object_reg[key]}  доступен!')
        logging.info(
            f'Регистратор на объекте: {key}  с ip адресом : {object_reg[key]} доступен.')
        continue
    else:
        print(f'Регистратор {object_reg[key]}  не доступен!')
        logging.info(
            f'Регистратор на объекте: {key}  с ip адресом : {object_reg[key]} не доступен.')
        break

object_cam = {
    "place 1": "address 1",
    "place 2": "address 2",
    "place 3": "address 3",
    "place 4": "address 4"
}

logging.warning(f'ПРОВЕРКА КАМЕР\n'
                f'ВРЕМЯ : {now.strftime("%Y-%m-%d-%H.%M")}')
for key in object_cam:
    if ping(object_cam[key], verbose=False, count=4).success():
        print(f'Камера {object_cam[key]}  доступна!')
        logging.info(
            f'Камера на объекте: {key}  с ip адресом : {object_cam[key]} доступна.')
    else:
        print(f'Камера {object_cam[key]}  не доступна!')
        logging.info(
            f'Камера на объекте: {key}  с ip адресом : {object_cam[key]} не доступна.')

object_mikrotik = {
    "place 1": "address 1",
    "place 2": "address 2",
    "place 3": "address 3",
    "place 4": "address 4"
}

for key in object_mikrotik:
    if ping(object_mikrotik[key], verbose=False, count=4).success():
        print(f'Узел {object_mikrotik[key]}  доступен!')
        logging.info(
            f'Микротик на объекте: {key}  с ip адресом : {object_mikrotik[key]} доступен.')
    else:
        print(f'Узел {object_mikrotik[key]}  не доступен!')
        logging.info(
            f'Микротик на объекте: {key}  с ip адресом : {object_mikrotik[key]} не доступен.')


# раздел с почтой

def send_email(addr_to, msg_subj, msg_text, files):
    addr_from = "mail.ru"  # Отправитель
    password = "password"  # Пароль

    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = addr_from  # Адресат
    msg['To'] = ", ".join(addr_to)  # Получатель
    msg['Subject'] = msg_subj  # Тема сообщения

    body = msg_text  # Текст сообщения
    msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст

    process_attachement(msg, files)

    # ======== Этот блок настраивается для каждого почтового провайдера отдельно ===============================================
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)  # Создаем объект SMTP
    # server.starttls()                                      # Начинаем шифрованный обмен по TLS
    # server.set_debuglevel(True)                            # Включаем режим отладки, если не нужен - можно закомментировать
    server.login(addr_from, password)  # Получаем доступ
    server.send_message(msg)  # Отправляем сообщение
    server.quit()  # Выходим
    # ==========================================================================================================================


def process_attachement(msg, files):  # Функция по обработке списка, добавляемых к сообщению файлов
    for f in files:
        if os.path.isfile(f):  # Если файл существует
            attach_file(msg, f)  # Добавляем файл к сообщению
        elif os.path.exists(f):  # Если путь не файл и существует, значит - папка
            dir = os.listdir(f)  # Получаем список файлов в папке
            for file in dir:  # Перебираем все файлы и...
                attach_file(msg, f + "/" + file)  # ...добавляем каждый файл к сообщению


def attach_file(msg, filepath):  # Функция по добавлению конкретного файла к сообщению
    filename = os.path.basename(filepath)  # Получаем только имя файла
    ctype, encoding = mimetypes.guess_type(filepath)  # Определяем тип файла на основе его расширения
    if ctype is None or encoding is not None:  # Если тип файла не определяется
        ctype = 'application/octet-stream'  # Будем использовать общий тип
    maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
    if maintype == 'text':  # Если текстовый файл
        with open(filepath) as fp:  # Открываем файл для чтения
            file = MIMEText(fp.read(), _subtype=subtype)  # Используем тип MIMEText
            fp.close()  # После использования файл обязательно нужно закрыть
    elif maintype == 'image':  # Если изображение
        with open(filepath, 'rb') as fp:
            file = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
    elif maintype == 'audio':  # Если аудио
        with open(filepath, 'rb') as fp:
            file = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
    else:  # Неизвестный тип файла
        with open(filepath, 'rb') as fp:
            file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
            file.set_payload(fp.read())  # Добавляем содержимое общего типа (полезную нагрузку)
            fp.close()
            encoders.encode_base64(file)  # Содержимое должно кодироваться как Base64
    file.add_header('Content-Disposition', 'attachment', filename=filename)  # Добавляем заголовки
    msg.attach(file)  # Присоединяем файл к сообщению


# Использование функции send_email()
addr_to = ['mail']
files = [
    f"C:\\Users\\*****\\PycharmProjects\\pythonProject\\{filename}"]  # Список файлов, если вложений нет, то files=[]

# files = ["file1_path",  # Список файлов, если вложений нет, то files=[]
#          "file2_path",
#          "dir1_path"]  # Если нужно отправить все файлы из заданной папки, нужно указать её

send_email(addr_to, 'Информация по оборудованию', '', files)
