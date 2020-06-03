# Можно объявить пустой список
empty_list = []
# можно объявить список и сразу заполнить его
friends = ['Max', 'Leo', 'Kate']
# тип списка - list
print(type(friends))
# Как и в строке для списка доступны индексы (начинаются с 0)
print('Второй друг', friends[1])
print('Первый друг с конца', friends[-1])
# так же можно применять срезы
print(friends[1:2])
print(friends[:2])
print(friends[1:])

print(len(friends))  # длина списка
friends.append('Ron')  # добавление в список

print(len(friends))
print(friends.pop())  # удаление последнего элемета списка
print(friends)

friends.clear()  # очистка списка
print(friends)
friends = ['Max', 'Leo', 'Kate']

friends.remove('Kate')  # удаление из списка
print(friends)
del friends[0]  # удаление элемента по индексу
print(friends)
