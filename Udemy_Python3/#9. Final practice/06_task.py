# Написать функцию, которая принимает на вход строку - римское число,
# а возвращает это число в арабском виде.
# Например, если передаём "XV" - должна вернуть 15, если передаём "IV" - должна вернуть 4.
#
# Вот список римских символов и их отображение на арабские числа:
#   I - 1
#   V - 5
#   X - 10
#   L - 50
#   C - 100
#   D - 500
#   M - 1000
#
# Варианты типа IIIV = 5-3 = 2 мы не рассматриваем.
# Хотя Римляне и пользовались иногда такими видами записей,
# но есть разная информация о приемлимости оных.
# В нашем ДЗ такие варианты мы не рассматриваем.
# Вот выдержка из wiki:
#   "Необходимо отметить, что другие способы «вычитания» недопустимы;
#   так, число 99 должно быть записано как XCIX, но не как IC."
#
# Подсказка. Для решения надо реализовать два правила:
#   - если большая цифра стоит перед меньшей, то они складываются (принцип сложения),
#   - если меньшая цифра стоит перед большей, то меньшая вычитается из большей (принцип вычитания).
#
# Защиту от некорректного ввода реализовать по вашему желанию
# (можно не делать, но для тренировки всегда полезно).

def parce_roman(roman: str):
    """
    The Functions convert Romans numbers to Arabic numbers.
    :param roman: type:str; input roman number.
    :return: type:int; output arabic number.
    """
    result = 0
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    roman = roman.upper()
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and romans[c] < romans[roman[i + 1]]:  # Protection against index out of range.
            result -= romans[c]
        else:
            result += romans[c]
    return result


def parce_roman_test():
    print(f'Te test of the function parce_roman begin...')
    print('#Test 1 was successful.' if parce_roman('XI') == 11 else '#Test 1 failed.')
    print('#Test 2 was successful.' if parce_roman('XVI') == 16 else '#Test 2 failed.')
    print('#Test 3 was successful.' if parce_roman('XIV') == 14 else '#Test 3 failed.')
    print('#Test 4 was successful.' if parce_roman('xXiV') == 24 else '#Test 4 failed.')


if __name__ == '__main__':
    parce_roman_test()
