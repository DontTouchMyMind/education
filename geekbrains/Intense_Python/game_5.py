import random

words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека',
              'шайба', 'олимпиада')

secret_world = random.choice(words_list)
print(secret_world)

gamer_world = ['*'] * len(secret_world)  # Вывод - список
print(''.join(gamer_world))  # Склеили строку, но в памяти он все равно список


error_counter = 0  # Количество попыток
# Добавим диалог с пользователем
while True:
    letter = input('Введите одну букву:').lower()  # Перевод в нижний регистр вне зависимости от ввода
    if len(letter) != 1 or not letter.isalpha():  # Проверка длинны ввода и явл-ся ли буквой
        continue

    if letter in secret_world:
        for idx, symbol in enumerate(secret_world):  # Нумерует символы
            # print(idx, symbol)
            if letter == symbol:
                gamer_world[idx] = letter
        # if '*' not in gamer_world:
        if gamer_world.count('*') == 0:  # Если нет *
            print('Вы победили')
            print('Было загаданно: ', secret_world.upper())
            break
    else:
        error_counter += 1
        print('Ошибок допущено:', error_counter)
        if error_counter == 8:
            print('Вы проиграли')
            break
    print(''.join(gamer_world))

print('попробуйте еще')
