# В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел.
# Если компьютер угадал число, игрок выбирает “победа”.
# Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”.
# Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
# Игра продолжается до тех пор пока компьютер не отгадает число.
# Примечание: Знаки “=”, “>” и “<” пользователь вводит с клавиатуры для общения с компьютером.
# Вы можете использовать этот способ или придумать свой.

import random

number = int(input('Enter a number between 0 and 100: '))
# print(number)
var_dialogs = None
a = 1
b = 100
comp_number = random.randint(a, b)
print(comp_number)
while var_dialogs != '=':
    var_dialogs = input('Enter your decision (Exam.">","<","="): ')
    if var_dialogs == '<':
        b = comp_number
        comp_number = random.randint(a, b)
        print(comp_number)
    elif var_dialogs == '>':
        a = comp_number
        comp_number = random.randint(a, b)
        print(comp_number)
print('Its WIN')
