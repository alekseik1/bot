import command_system
import subprocess
from vkapi import get_wall_posts
from settings import token
from random import sample


def quotation(body=""):
    n = 3
    posts = get_wall_posts(token, '-128692347')
    # Отбираем 100 рандомных постов
    posts = sample(posts, 100)
    # Чистим посты от #..
    posts = list(map(lambda x: x[:x.find('#')], posts))
    cmd = "cd markov-text; echo \'{}\' >> speech.txt;" \
          " python markov.py parse quote 2 speech.txt; " \
          "python markov.py gen qoute {};".format('\n'.join(posts), n)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    message = out.decode('utf-8')
    attachment = ''
    print("message is: " + message)
    return message, attachment


pryt_command = command_system.Command()

pryt_command.keys = ['цитата', 'цитата препода', 'что скажет препод', 'как говорят в мфти']
pryt_command.description = 'Цитаты за жизнь'
pryt_command.process = quotation
