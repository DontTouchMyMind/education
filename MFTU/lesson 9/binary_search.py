# Важно! Массив должен быть отсортирован.
# Допустим, что массив отсортирован по возрастанию,
#   где левая граница указывает на элемент, который меньше искомого,
#   правая граница указывает на элемент, который больше искомого.
# Искать границы будем в разных функциях.

def left_bound(input_list, key):
    left = -1
    right = len(input_list)
    while (right - left) > 1:
        middle = (left + right) // 2
        if input_list[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(input_list, key):
    left = -1
    right = len(input_list)
    while (right - left) > 1:
        middle = (left + right) // 2
        if input_list[middle] <= key:
            left = middle
        else:
            right = middle
    return right


list1 = [1, 3, 3, 6, 7, 9]

l = left_bound(list1, 6)
r = right_bound(list1, 6)
print(l, r)
