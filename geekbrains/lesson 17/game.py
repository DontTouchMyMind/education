import random


def game():
    number = random.randint(1, 100)
    user_number = None
    count = 0
    level = int(input('Выберети уровень сложности:  '))
    levels = {
        1: 10,
        2: 5,
        3: 3
    }
    print(number)
    max_count = levels[level]

    user_count = int(input('Введите кол-во пользователей: '))
    users = []
    for i in range(user_count):
        user_name = input(f'Введите Имя Пользователя {i + 1}: ')
        users.append(user_name)
    # print(users)

    is_winner = False
    winner_name = None

    while not is_winner:
        count += 1
        if count > max_count:
            print('Все пользователи проиграли!')
            break
        print(f'Попытка № {count}')

        for user in users:
            print(f'Ход пользователя {user} ')
            user_number = int(input('Введите число: '))
            if user_number == number:
                is_winner = True
                winner_name = user
                break
            elif number < user_number:
                print(' Ваше число больше загаданного!')
            else:
                print('Ваше число меньше загаданного!')
    else:
        print(f'Победитель {winner_name} ')
