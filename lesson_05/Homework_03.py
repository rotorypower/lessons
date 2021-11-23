"""аписать функцию, которая используя модуль requests скачивает файл сохраняет
его на файловой системе, функция имеет два параметра: ссылка на файл и имя на
файловой системе. В качестве примера ссылки на файл можно использовать лицензию из
ГитХаба из вашего репозитория: https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE"""

import requests

def my_func(save, link):
    file = open(save,"wb")
    opened = requests.get(link)
    file.write(opened.content)
    file.close()
my_func(save="/home/kavalevskiyuri", link="https://github.com/rotorypower/lessons/blob/master/README.txt")