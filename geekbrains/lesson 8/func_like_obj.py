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


def my_filter(numbers):
    my_result = []
    for number in numbers:
        if number % 2 == 0:
            my_result.append(number)
    return my_result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_filter(numbers))


