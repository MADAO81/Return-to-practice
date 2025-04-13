import threading
import time

import requests

urls = [
    'https://yandex.ru',
    'https://google.com',
    'https://pgu.mos.ru',
    'https://www.auchan.ru/',
    'https://vk.com',
    #'https://www.perekrestok.ru/',
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
loaded_pages_lock = threading.Lock()  # ещё называют mutex

class PageLoader(threading.Thread):
    def __init__(self, url):
        self.url = url
        super().__init__()  # вызвали родительский конструктор

    def run(self):
        text = requests.get(self.url).text

        loaded_pages_lock.acquire()
        loaded_pages.append(text)
        loaded_pages_lock.release()

class Progress(threading.Thread):
    def run(self):

        while True:
            loaded_pages_lock.acquire()  # если занято соседним потоком, то будет ждать
            n = len(loaded_pages)
            loaded_pages_lock.release()

            if n == len(urls):
                break

            print(f'Загружено {n} из {len(urls)}')
            time.sleep(1)

        print('Загрузили всё')

progress = Progress()

page_loaders = []
for url in urls:
     page_loaders.append(PageLoader(url))

print('Начинаем')

progress.start()
for page_loader in page_loaders:
    page_loader.start()

print('Заканчиваем (но не здесь)')

progress.join()  # ждём конца

for page_loader in page_loaders:
    page_loader.join()

print('А теперь точно закончили')
