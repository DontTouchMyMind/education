def some_f():
    return 10


result = some_f()   # The result will be argument of function ('10')
print(result)       # type is int

a = some_f          # 'a' is function

print(a)


def f():
    print('Hello from other f')


def to(f_param):
    f_param()


to(f)


def my_filter(numbers, function):
    my_result = []
    for number in numbers:
        if function(number):        # if function (examp.'is_even') is right, the True
            my_result.append(number)
    return my_result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(number):
    return number % 2 == 0


def is_not_even(number):
    return number % 2 != 0


def big4(number):
    return number > 4


print(my_filter(numbers, is_not_even))
print(my_filter(numbers, is_even))
print(my_filter(numbers, big4))
print(my_filter(numbers, lambda number: number % 3 == 0))

