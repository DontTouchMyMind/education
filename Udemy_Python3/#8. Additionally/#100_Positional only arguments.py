x = float('2.1')
print(x)


def avg(a, b, c):
    return (a + b + c) / 3


print(avg(1, 2, 3))  # Вызов с использованием позиционных аргументов.
print(avg(a=1, b=2, c=3))  # Вызов с использованием имен.


# Такой вызов можно запретить и разрешить передавать значения в функцию только позиционно.


def avg_only_position(a, b, c, /):  # Все переменные до / объявлятся только позиционированием.
    return (a + b + c) / 3


print(avg_only_position(1, 2, 3))


# print(avg_only_position(a=1, b=2, c=3))

# Можно разрешить передачу аргументов разными способами.
def assert_equal(left, right, /, fail_message=''):
    return (left == right, fail_message)


assert_equal(1, 1)
assert_equal(1, 2, fail_message='left not equals right')


def copy_func(*, source, destination, overwrite=False):
    # Все переменные после * объявлятся только с использованием имен.
    print(f'Copying {source} to {destination} with overwrite={overwrite}')


# copy_func('C://tmp//file1.txt', 'C://tmp//file1_copy.txt', True)
copy_func(source='C://tmp//file1.txt', destination='C://tmp//file1_copy.txt', overwrite=True)


def copy_func_mix(source, destination, /, *, overwrite=False):
    print(f'Copying {source} to {destination} with overwrite={overwrite}')


copy_func_mix('C://tmp//file1.txt', 'C://tmp//file1_copy.txt', overwrite=True)
