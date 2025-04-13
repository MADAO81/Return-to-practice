import requests  # нужно установить: pip install requests
import threading

def load_all_pages():
    urls = [
        'https://yandex.ru',
        'https://google.com',
        'https://pgu.mos.ru',
        'https://www.auchan.ru/',
        'https://vk.com',
        'https://www.perekrestok.ru/',
        'https://ok.ru/',
        #'https://tutu.ru'
    ]
    for site in urls:
        print('Загружаем', site)
        text = requests.get(site).text

print('Начали основную программу')
#load_all_pages()
threading.Thread(target=load_all_pages).start()
print('Закончили основную программу')
