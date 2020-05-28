# Sorting Tony Hoar
def hoar_sort(A):
    """
    Function sorts input-list
    :param A: input-list
    :return: sorted list
    """
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1


input_list = [5, 7, 2, 8, 3, 10, 1]
hoar_sort(input_list)
print(*input_list)
