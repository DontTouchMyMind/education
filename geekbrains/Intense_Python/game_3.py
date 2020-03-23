import random

words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека',
              'шайба', 'олимпиада')

secret_world = random.choice(words_list)
print(secret_world)

gamer_world = ['*'] * len(secret_world)  # Вывод - список
print(''.join(gamer_world))  # Склеили строку, но в памяти он все равно список

# gamer_world[1] = 'г'
# print(''.join(gamer_world))
error_counter = 0
# Добавим диалог с пользователем
while True:
    letter = input('Введите одну букву').lower()  # Перевод в нижний регистр вне зависимости от ввода
    if len(letter) != 1 or not letter.isalpha():  # Проверка длинны ввода и явл-ся ли буквой
        continue

    if letter in secret_world:
        pass
    else:
        error_counter += 1
        print('Ошибок допущено:', error_counter)
        if error_counter == 8:
            print('Вы проиграли')
            break
    print(''.join(gamer_world))

print('попробуйте еще')
