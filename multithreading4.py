import requests  # нужно установить: pip install requests
import threading

class PageLoader(threading.Thread):
    urls = [
        'https://yandex.ru',
        'https://google.com',
        'https://pgu.mos.ru',
        'https://www.auchan.ru/',
        'https://vk.com',
        'https://www.perekrestok.ru/',
        'https://ok.ru/',
        # 'https://tutu.ru'
    ]

    def run(self):  # переопределяем метод run() родителя
        for site in self.urls:
            print('Загружаем', site)
            text = requests.get(site).text

print('Начали основную программу')
page_loader = PageLoader()
page_loader.start()  # не путать с run()
print('Закончили основную программу')
