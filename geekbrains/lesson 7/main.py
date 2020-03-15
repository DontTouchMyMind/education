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

user_number = int(input('Enter a number between 0 and 100: '))
result = None
min_result = 0
max_result = 100

while result != '=':
    number = random.randint(min_result, max_result)
    print(number)
    result = input('Enter your decision (Exam.">","<","="): ')
    if result == '<':
        max_result = number - 1
    elif result == '>':
        min_result = number + 1
print('Its WIN')
