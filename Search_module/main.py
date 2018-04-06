import os
from datetime import datetime
from multiprocessing import Process
import time


from parsers.cyberleninka import cyberleninka
from parsers.scholar import scholar
from parsers.socionet import socionet
#  from config import *


def main(author, title, keywords, year1, year2):
    timestamp_dir = datetime.now().strftime('%Y-%m-%d-%H-%M')
    base_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = base_dir + '/data/' + timestamp_dir + '/' + 'documents'
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    time_start = time.time()
    p1 = Process(target=cyberleninka, args=(base_dir, author, title, keywords, year1, year2))
    p2 = Process(target=scholar, args=(base_dir, author, title, keywords, year1, year2))
    p3 = Process(target=socionet, args=(base_dir, author, title, keywords, year1, year2))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    for file in os.listdir(base_dir):
        file_name = base_dir + '/' + file
        if os.stat(file_name).st_size < 5:
            os.remove(file_name)
    time_end = time.time()
    with open('/'.join(base_dir.split('/')[:2]) + '/log.txt', 'a', encoding='utf-8') as log:
        log.write('Дата запроса: ' + timestamp_dir + '\n')
        log.write('Файлов загружено: ' + str(len(os.listdir(base_dir))) + '\n')
        log.write('Время затраченное: ' + str(time_end - time_start) + '\n')
        log.write('-Автор: ' + author + '\n')
        log.write('-Название работы: ' + title + '\n')
        log.write('-Ключевые слова: ' + keywords + '\n')
        log.write('-Дата: ' + year1 + ' - ' + year2 + '\n')
        log.write('='*30 + '\n')


def test():
    author = 'Черненький М. В.'
    title = ''
    keywords = 'метод'
    year1 = ''
    year2 = ''
    main(author, title, keywords, year1, year2)


if __name__ == '__main__':
    test()
