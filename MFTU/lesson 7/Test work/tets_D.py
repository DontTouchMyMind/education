# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение наибольшего четного элемента последовательности.
# Числа, следующие за нулем, считывать не нужно.
#
# Формат входных данных
#   Последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
#   Каждое число на новой строке.
#
# Формат выходных данных
#   Одно число — максимальное четное число в последовательности,
#   если четные числа в ней присутствуют, иначе - 0.

numbers = []

while True:
    number = int(input())
    if number == 0:
        break
    numbers.append(number)

result = [number for number in numbers if number % 2 == 0]
result.sort(reverse=True)
try:
    print(result[0])
except IndexError:
    print(0)
