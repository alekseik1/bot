import command_system
import subprocess


def pryt():
    message = ''
    n = 3
    cmd = "cd markov-text; python markov.py parse pryt 2 speech.txt; python markov.py gen pryt {};".format(n)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    message = out.decode('utf-8')
    attachment = ''
    print("message is: " + message)
    return message, attachment


pryt_command = command_system.Command()

pryt_command.keys = ['прутизм', 'прутавизм', 'прут', 'pryt']
pryt_command.description = 'Прутизмы на каждый день'
pryt_command.process = pryt
