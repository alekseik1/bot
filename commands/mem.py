import command_system
import vkapi


def mem(body=""):
   # Получаем случайную картинку из пабли
   attachment = vkapi.get_random_wall_picture(-145641262)
   message = 'Picture from stena pablika.\n Ya lyblu memasi'
   return message, attachment

mem_command = command_system.Command()

mem_command.keys = ['мем', 'мемес', 'боян', 'картинка', 'развлечение', 'удиви меня', 'mem', 'meme']
mem_command.description = 'Send kartinka with some memes'
mem_command.process = mem
