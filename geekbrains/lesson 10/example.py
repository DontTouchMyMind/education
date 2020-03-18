# В зависимости от параметра вызвать различные функции скрипта
# Параметр ping -> функция выводит pong
# 2 параметра name <Имя> -> функция приветствует пользователя
# параметр list показать содержимое текущей дириктории

import sys, os


def ping():
    print('Pong')


def hello(name):
    print('Hello', name)


def get_info():
    print(os.listdir())


command = sys.argv[1]

if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name)
