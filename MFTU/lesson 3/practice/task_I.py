# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение наибольшего элемента последовательности.
#
# Числа, следующие за нулем, считывать не нужно.
#
# Формат входных данных
#   Вводится последовательность целых чисел,
#   оканчивающаяся числом 0 (само число 0 в последовательность не входит).
#
# Формат выходных данных
#   Выведите ответ на задачу (одно число).

my_list = []
number = 1
while number != 0:
    number = int(input())
    my_list.append(number)
print(max(my_list))
