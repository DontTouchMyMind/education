# Даны два произвольных списка.
# Удалите из первого списка элементы присутствующие во втором.
my_list_1 = [2, 5, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for num in my_list_2:
    while num in my_list_1:
        my_list_1.remove(num)
print(my_list_1)

for num in my_list_1[:]:        # Сделаем срез списка от начала и до конца
    if num in my_list_2:        # И будем работать с копией списка
        my_list_1.remove(num)   # Такой срез можно делать только при .remove()
print(my_list_1)
