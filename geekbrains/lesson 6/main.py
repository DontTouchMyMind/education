import random

number = random.randint(1, 100)
user_number = None
count = 0
level = int(input('Выберети уровень сложности:  '))
levels = {
    1:10,
    2:5,
    3:3
}
#print(number)
max_count = levels[level]
while number != user_number:
    count += 1
    if count > max_count:
        print('You lose')
        break
    print(f'Попытка {count}')
    user_number = int(input('Введите число: '))
    if number < user_number:
        print('your number is big')
    elif number > user_number:
        print('your number is small')
else:
    print('Win')