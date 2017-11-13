import command_system
import vkapi
import random

def random_answer():
    #r = random.seed()
    n = random.randint(1, 3)
    if n == 1:
        attachment = ''
        attachment = vkapi.get_random_wall_image(-27456813)
        message = 'PACANY OTVETYAT'
    elif n == 2:
        attachment = vkapi.get_random_wall_image(-1)
        message = 'Sorry for content. My boss is still a bad programmer :('
    elif n == 3:
        attachment = ''
        message = "I'm tired. Let me relax..."
    return message, attachment

r_command = command_system.Command()

r_command.keys = ['удиви меня', 'some text', 'что расскажешь', 'расскажи', 'как дела', 'как жизнь', 'расскажи историю', 'историю']
r_command.description = 'Send random thing'
r_command.process = random_answer
