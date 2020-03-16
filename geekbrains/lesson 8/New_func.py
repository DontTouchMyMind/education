# Модуль числа
print(abs(-7))  # Результат 7

# min, max
numbers = [5, 15, 7, 1, -9, 0]
print(max(numbers))
print(min(numbers))

# round - округляем число до определенного кол-ва знаков после запятой
print(round(10.9872, 2))    # Результат 10.99
# sum
print(sum(numbers))

# enumerate - "1" - число с которого будем стартовать, по умолч. 0
winners = ['Loe', 'Max', 'Kate']
for number, winner in enumerate(winners, 1):
    print(number, winner)
# в цикле перебирается переменные, где number - номер элемента, winner - сам элемент последовательности

# Пример
# Пользователь вводит 3 числа
# Найти минимальное из них, максимальное из них, их сумму и вывести результат на экран

user_numbers = []   # Создаем пустой контейнер
for i in range(3):
    var_num = int(input('Enter your number: '))
    user_numbers.append(var_num)
print('Max sequence value ', max(user_numbers))
print('Min sequence value ', min(user_numbers))
print('Sum of sequence values ', sum(user_numbers))

