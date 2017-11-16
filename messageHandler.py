import vkapi
import os
import importlib
from command_system import command_list

def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1
    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition
    return d[lenstr1 - 1, lenstr2 - 1]


def load_modules():
    files = os.listdir("commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])

'''
Извиниться за предыдущее и сообщить о перезаливе
@param: ids id пользователей, которым надо разослать
'''
def sorry(token):
    ids = vkapi.get_previous_interlocutors(token)
    message = "Привет :)\nЯ, возможно, написал тебе кучу дряни. Хочу извиниться, ведь я всего лишь бездумно учился у других. Теперь же меня перезалили. Я начну учиться правильно, обещаю!"
    for user_id in ids:
        vkapi.send_message(user_id, token, message, '')


def get_answer(data):

    # Maintainance mode
    m_mode = True
    if m_mode:
        if(data['user_id'] != 92540660):
            message = "Прости, но я сейчас в режиме обслуживания. Не могу говорить, ботаю теорфиз"
            attachment = ''
            return message, attachment

    data = data['body'].lower()

    message = "TOO SLOZHNA. Let me write some random text"
    attachment = ""
    distance = len(data)
    command = None
    key = ""
    for c in command_list:
        for k in c.keys:
            d = damerau_levenshtein_distance(data, k)
            if d < distance:
                distance = d
                command = c
                key = k
                if distance == 0:
                    message, attachment = c.process()
                    return message, attachment
    if distance < len(data)*0.4:
        message, attachment = command.process()
        #message = 'Ya CLEVER. Pohozhe, ti napisal "%s"\n\n' % key + message
    else:
        command = None
        # ВЫПУСКАЙТЕ ПРУТА!
        for c in command_list:
            if 'pryt' in c.keys:
                command = c
                break
        message, attachmet = command.process(data)  # Теперь генератор обрабатывает вашу речь. Бойтесь ИИ!
    print("message is: " + message)
    return message, attachment



def create_answer(data, token):
    load_modules()
    user_id = data['user_id']
    print("Data came: ", data) # Debug print.
    message, attachment = get_answer(data)
    # Извинимся 1 раз
    do_once = True
    #if do_once:
      #  sorry(token)
       # do_once = False

    vkapi.send_message(user_id, token, message, attachment)

# TODO: Сохранение файлов между сессиями
