import command_system
import requests as req
from bs4 import BeautifulSoup
import re


def get_solutions(course, task: list):
    site = 'https://mipt1.ru/1_2_3_4_5_kor.php?sem=%d&zad={}' % course
    for t in task:
        # Get page
        r = req.get(site.format(t))
        r.encoding = 'cp1251'
        soup = BeautifulSoup(r.text, 'html.parser')
        res = re.findall(r'\d+!', soup.b.text)
        if res:
            page = res[0][:-1]
        else:
            page = ''
        return page


def kor(body=""):
    sem_and_task = re.findall(r'\d+\.?\d*', body)
    if len(sem_and_task) != 2:
        return 'Некорректный запрос! Нужно писать номер семестра и номер задачи', ''
    if re.findall(r'\.', sem_and_task[0]):
        task = sem_and_task[0]
        sem = sem_and_task[1]
    elif re.findall(r'\.', sem_and_task[1]):
        task = sem_and_task[1]
        sem = sem_and_task[0]
    else:
        return 'Некорректный запрос! Нужно писать номер семестра и номер задачи', ''

    if sem not in [1, 2, 3, 4, 5]:
        return 'Я не смогу найти задачи для этого семестра!', ''
    if task:
        try:
            page = get_solutions(sem, [task])
        except:
            return 'Некорректный запрос! Нужно писать номер семестра и номер задачи', ''
    else:
        return 'Я не смог найти эту задачу в Корявове!'
    if page:
        return 'Задача {} найдена на странице {}'.format(task, page), ''
    else:
        return 'Задача не найдена в Корявове!'


kor_command = command_system.Command()

kor_command.keys = ['Задача 4 1.11', 'найти в корявове 4 1.11', 'поиск в коряове 4 1.11', 'корявов 4 1.11']
kor_command.description = 'Поиск задачи в корявове'
kor_command.process = kor
