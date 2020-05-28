def check_sorted(A, ascending=True):
    """
    Проверка отсортированности за О(len(A))
    Function checks array sorting for O(n)
    :param A:
    :param ascending:
    :return:
    """
    flag = True
    s = 2 * ascending - 1
    for i in range(0, len(A) - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag


list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [6, 5, 4, 3, 2, 1]
list_3 = [1, 2, 4, 3, 6, 5]

print(check_sorted(list_1))
print(check_sorted(list_2, ascending=False))
print(check_sorted(list_3))
