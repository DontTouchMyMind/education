# Шаг 1. Загадать случайное число
import random   # подключили библиотеку

number = random.randint(1, 100)
user_number = None
count = 0
#print(number)
while number != user_number:
    # Шаг 2. Предложить пользователю ввести число
    count += 1
    print(f'Попытка {count}')
    user_number = int(input('Введите число: '))
    # Шаг 3. Сравнить данные и вывести результат
    if number < user_number:
        print('your number is big')
    elif number > user_number:
        print('your number is small')
    # Шаг 4. Реализовать цикл

print('Win')