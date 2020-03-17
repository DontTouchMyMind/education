# Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»


def main_func(name, age, city):
    data = str('{}, {} год(а), проживает в городе {}'.format(name, age, city))
    return data


# Validating of function
var = main_func('Василий', '21', 'Москва')
print(main_func('max', 33, 'London'))
print(var)
print(type(var))
