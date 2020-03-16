# Функция простой разделитель
# Необходимо заменить повторяющие действия,
# т.к. если в них будут ошибки, они могут множиться
# У функции нет возращаемого значения
def print_sep(sep, sep_len):    # название_функции (вводные параметры)
    print(sep * sep_len) # тело функции

# print('My first function')
# print_sep()
# print('Good separators')
# print_sep()
# print('What is there are a lot of them?')
# print_sep()
# print_sep()
# print_sep()

# We can change the separator, if we will change input variable
print_sep('*', 100)
print_sep('-', 100)
# we can change the separator and length
print_sep('+', 50)
result = print_sep('-', 100)
print(result)   # Результат будет None(cм. строку 4)
#
#

