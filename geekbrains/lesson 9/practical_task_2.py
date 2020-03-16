# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
numbers = [2, 4, 15]


def max_func(a, b, c):
    out = max(a, b, c)
    return out


max_func(numbers[0], numbers[1], numbers[2])

print(max_func(numbers[0], numbers[1], numbers[2]))

# Simple Code
print(max(numbers[0], numbers[1], numbers[2]))
