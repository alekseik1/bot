import command_system
import requests as req
from bs4 import BeautifulSoup
import re
from warnings import warn


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


err_msg = 'Некорректный запрос! Нужно писать номер семестра и номер задачи'

DEFAULT_SEMESTER = 4

def _parse_sem_and_task(sem_and_task: list):
    if len(sem_and_task) == 2:
        # 2 passed parameters
        if re.findall(r'\.', sem_and_task[0]):
            task = sem_and_task[0]
            sem = sem_and_task[1]
        elif re.findall(r'\.', sem_and_task[1]):
            task = sem_and_task[1]
            sem = sem_and_task[0]
        else:   # Bad parsing
            raise ValueError(err_msg)
        try:
            sem = int(sem)
        except ValueError:
            raise ValueError(err_msg)
    elif len(sem_and_task) == 1:
        # 1 passed parameter
        if re.findall(r'\.', sem_and_task[0]):
            task = sem_and_task[0]
            sem = DEFAULT_SEMESTER
        elif re.findall(r'\.', sem_and_task[1]):
            task = sem_and_task[1]
            sem = DEFAULT_SEMESTER
        else:   # Bad parsing
            raise ValueError(err_msg)
    else:   # len(sem_and_task) is not 1 or 2
        raise ValueError(err_msg)
    return sem, task

def kor(body=""):
    sem_and_task = re.findall(r'\d+\.?\d*', body)
    try:
        sem, task = _parse_sem_and_task(sem_and_task)
    except ValueError as e:
        return str(e), ''
    print("Got sem_and_task {}; Got sem {}; got task {}".format(sem_and_task, sem, task))

    if sem not in [1, 2, 3, 4, 5]:
        return 'Я не смогу найти задачи для этого семестра!', ''
    if task:
        try:
            page = get_solutions(sem, [task])
        except:
            return 'Что-то пошло не так. Ты уверен, что написал номер семестра и номер задачи?', ''
    else:
        return 'Я не смог найти эту задачу в Корявове!'
    if page:
        return 'Задача {} найдена на странице {}\nСкажите спасибо mipt1.ru'.format(task, page), ''
    else:
        return 'Задача не найдена в Корявове!', ''


kor_command = command_system.Command()

kor_command.keys = ['Задача 4 1.11', 'найти в корявове 4 1.11', 'поиск в коряове 4 1.11', 'корявов 4 1.11',

                    'Задача 4 семестр 1.11', 'найти в корявове 4 семестр 1.11', 'поиск в коряове 4 семестр 1.11',
                    'корявов 4 семестр 1.11',

                    'найти в корявове 4 1.11 задача', 'поиск в коряове 4 1.11 задача', 'корявов 4 1.11 задача',

                    'Задача 4 семестр 1.11', 'найти в корявове 4 семестр 1.11 задача',
                    'поиск в коряове 4 семестр 1.11 задача', 'корявов 4 семестр 1.11 задача',

                    # Кор
                    'Задача 4 1.11', 'найти в коре 4 1.11', 'поиск в кор 4 1.11', 'кор 4 1.11',

                    'Задача 4 семестр 1.11', 'найти в кор 4 семестр 1.11', 'поиск в кор 4 семестр 1.11',
                    'кор 4 семестр 1.11',

                    'найти в кор 4 1.11 задача', 'поиск в кор 4 1.11 задача', 'кор 4 1.11 задача',

                    'Задача 4 семестр 1.11', 'найти в кор 4 семестр 1.11 задача',
                    'поиск в кор 4 семестр 1.11 задача', 'кор 4 семестр 1.11 задача',

                    # Кор без семестра
                    'Задача 1.11', 'найти в коре 1.11', 'поиск в кор 1.11', 'кор 1.11',

                    'Задача cеместр 1.11', 'найти в кор cеместр 1.11', 'поиск в кор cеместр 1.11',
                    'кор cеместр 1.11',

                    'найти в кор 1.11 задача', 'поиск в кор 1.11 задача', 'кор 1.11 задача',

                    'Задача cеместр 1.11', 'найти в кор cеместр 1.11 задача',
                    'поиск в кор cеместр 1.11 задача', 'кор cеместр 1.11 задача'
                    ]
kor_command.description = 'Поиск задачи в корявове'
kor_command.process = kor
