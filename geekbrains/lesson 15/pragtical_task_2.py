# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.
# Примечание: Список с целыми числами создайте вручную в начале файла.
# Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 45, 39, 28, 21, 20, 79, 88, -100500]

# multiple 3
result_mult = [number for number in numbers if number % 3 == 0]
print(result_mult)

# Positive elements
result_pos = [number for number in numbers if number > 0]
print(result_pos)

# Not multiple 4
result_not_mult = [number for number in numbers if number % 4 != 0]
print(result_not_mult)

# All conditions in one generator
result = [number for number in numbers if number > 0 and number == 3 and number != 4]
print(result)
