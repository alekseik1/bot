import vkapi
import os
from command_system import command_list

def get_answer(body):
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    attachment = ''
    return message, attachment



def create_answer(data, token):
   user_id = data['user_id']
   message, attachment = get_answer(data['body'].lower())
   vkapi.send_message(user_id, token, message, attachment)

