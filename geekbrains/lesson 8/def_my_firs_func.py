# Функция простой разделитель
# Необходимо заменить повторяющие действия,
# т.к. если в них будут ошибки, они могут множиться
# У функции нет возращаемого значения

def print_sep(sep, sep_len):    # название_функции (вводные параметры)
    print(sep * sep_len)        # тело функции


def get_sep(sep, sep_len):
    return (sep * sep_len)

# We can change the separator, if we will change input variable
print_sep('*', 100)
print_sep('-', 100)
# We can change the separator and length
print_sep('+', 50)
# result = print_sep('-', 100)
# print(result)  # Результат будет None(cм. строку 4)
# Use the separator in the text
result_func = get_sep('~', 50)
text = 'Hello {} Func {}'.format(result_func, result_func)
print(text)
