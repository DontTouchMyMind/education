import random


def game_reverse():
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

    return print('Its WIN')
