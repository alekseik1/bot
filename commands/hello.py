import command_system


def hello():
   message = 'Welcome, wanderer.\n 8ka Inc. is happy to meet you'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте', 'privet']
hello_command.description = 'HELLO FROM ME'
hello_command.process = hello
