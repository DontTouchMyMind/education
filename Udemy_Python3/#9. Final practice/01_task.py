# Напишите функцию count_vowels, которая принимает строку и возвращает количество гласных в ней.

def count_vowels(input_str: str):
    count = 0
    for letter in input_str:
        if letter in 'aeio':
            count += 1
    return count


def count_vowels_test():
    print(f'Te test of the function count_vowels begin...')
    print('#Test 1 was successful.' if count_vowels('aioe') == 4 else '#Test 1 failed.')
    print('#Test 2 was successful.' if count_vowels('awqqse') == 2 else '#Test 2 failed.')
    print('#Test 3 was successful.' if count_vowels('qqqqqqqq eqqqq i  o') == 3 else '#Test 3 failed.')
    print('#Test 4 was successful.' if count_vowels('') == 0 else '#Test 4 failed.')


if __name__ == '__main__':
    count_vowels_test()
