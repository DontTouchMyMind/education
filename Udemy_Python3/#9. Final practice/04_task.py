# Написать функцию check_sequence, принимающую список целых чисел и возвращающую
# 1 если последовательность строго возрастающая,
# -1 если строго убывающая, 0 если ни то, ни другое.
def check_sequence(input_list: list):
    if sorted(set(input_list)) == input_list:
        return 1
    if sorted(set(input_list), reverse=True) == input_list:
        return -1
    return 0


def check_sequence_test():
    print(f'Te test of the function check_sequence begin...')
    print('#Test 1 was successful.' if check_sequence([1, 2, 3]) == 1 else '#Test 1 failed.')
    print('#Test 2 was successful.' if check_sequence([3, 2, 1]) == -1 else '#Test 2 failed.')
    print('#Test 3 was successful.' if check_sequence([1, 2, 1]) == 0 else '#Test 3 failed.')
    print('#Test 4 was successful.' if check_sequence([1, 1]) == 0 else '#Test 4 failed.')


if __name__ == '__main__':
    check_sequence_test()
