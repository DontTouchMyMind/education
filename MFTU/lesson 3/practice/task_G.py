# Определите сумму всех элементов последовательности, завершающейся числом 0.
#
# Числа, следующие за нулем, считывать не нужно.
#
# Формат входных данных
#   Вводятся элементы последовательности по одному целому числу на строку.
#   Числа вводятся, пока не будет введен 0.
#
# Формат выходных данных
#   Вывести одно целое число - сумму последовательности.

sum_numbers = 0
number = 1
while number != 0:
    number = int(input())
    sum_numbers += number
print(sum_numbers)
