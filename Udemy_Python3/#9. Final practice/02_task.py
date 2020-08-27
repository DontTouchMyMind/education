# Написать функцию is_full_house, которая принимает список карт (руку, 5 карт иначе говоря)
# и определяет наличие комбинации Full House на руке.
# Возвращает True, если определён Full House, в противном случае - False.
# Full House это когда из пяти карт 2 одного достоинства и 3 одного достоинства (но отличающегося от пары).
# A - туз, J - валет, Q - дама, K - король, 2-10.
# Примеры Full House: (A, A, Q, Q, Q), (10, 10, 10, J, J)

def is_full_house(hand: list) -> bool:
    return all([hand.count(i) >= 2 for i in hand])


def is_full_house_test():
    print(f'Te test of the function is_full_house begin...')
    print('#Test 1 was successful.' if is_full_house(['A', 'A', 'A', 'K', 'K']) is True else '#Test 1 failed.')
    print('#Test 2 was successful.' if is_full_house(['3', 'J', 'J', 'J', '3']) is True else '#Test 2 failed.')
    print('#Test 3 was successful.' if is_full_house(['3', '4', '2', 'J', '3']) is False else '#Test 3 failed.')
    print('#Test 4 was successful.' if is_full_house(['J', 'J', 'J', 'J', '3']) is False else '#Test 4 failed.')


if __name__ == '__main__':
    is_full_house_test()
