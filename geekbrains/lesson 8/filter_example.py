numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)


def is_even(number):
    return number % 2 == 0


result = filter(is_even, numbers)
print(list(result))

names = ['', 'Max', 'Kate', 'Rich', 'Any']

print(list(filter(lambda x: len(x) > 3, names)))
