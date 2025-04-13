import threading
import time

import requests

urls = [
    'https://yandex.ru',
    'https://google.com',
    'https://pgu.mos.ru',
    'https://www.auchan.ru/',
    'https://vk.com',
    'https://www.perekrestok.ru/',
    'https://ok.ru/',
    'https://meet.goto.com/',
    'https://mail.ru',
    'https://stackoverflow.com/',
    'https://github.com',
    'https://python.org',
    'https://cisco.com',
    'https://python.org',
    'https://www.autodesk.ru/',
    'https://www.tinkoff.ru/'
    'https://www.microsoft.com/ru-ru',
    'https://www.gazprombank.ru/'
]

loaded_pages = []

class PageLoader(threading.Thread):
    def run(self):
        for url in urls:
            text = requests.get(url).text
            loaded_pages.append(text)

class Progress(threading.Thread):
    def run(self):
        while len(loaded_pages) < len(urls):  # Опасно, потому что в loaded pages пишет соседний поток
            print(f'Загружено {len(loaded_pages)} из {len(urls)}')
            time.sleep(1)
        print('Загрузили всё')

progress = Progress()
page_loader = PageLoader()

print('Начинаем')

progress.start()
page_loader.start()

print('Заканчиваем (но не здесь)')

progress.join()  # ждём конца
page_loader.join()

print('А теперь точно закончили')
