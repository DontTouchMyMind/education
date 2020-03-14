# Шаг 1. Загадать случайное число
import random   # подключили библиотеку

number = random.randint(1, 100)
print(number)

# Шаг 2. Предложить пользователю ввести число
user_number = int(input('Введите число: '))

# Шаг 3. Сравнить данные и вывести результат
if number == user_number:
    print('Win')
elif:
    print('Lose')
else:
    print('else_error')
