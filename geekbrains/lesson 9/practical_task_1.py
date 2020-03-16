# Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»


def main_func(name, age, city):
    data = str((name, ',', age, 'год(а),', 'проживает в городе', city))
    return data


# Validating of function
var = main_func('Василий', '21', 'Москва')

print(var)
print(type(var))
