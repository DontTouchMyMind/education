# Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def main_func(name, age, city):
    print(name, ',', age, 'год(а),', 'проживает в городе', city)


main_func('Василий', '21', 'Москва')
print(type(main_func))