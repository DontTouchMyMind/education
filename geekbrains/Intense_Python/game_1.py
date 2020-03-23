import random

words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека',
              'шайба', 'олимпиада')

secret_world = random.choice(words_list)
print(secret_world)

gamer_world = ['*'] * len(secret_world)  # Вывод - список
print(''.join(gamer_world))  # Склеили строку, но в памяти он все равно список

# gamer_world[1] = 'г'
# print(''.join(gamer_world))
