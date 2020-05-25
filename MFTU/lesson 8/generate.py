def generate_number(N:int, M:int, prefix=None):
    """
    Генерирует все числа (с лидирующими нулями)
    в N-ричной системе счисления(N <= 10) длины M
    :param N:
    :param M:
    :param prefix:
    :return:
    """
    prefix = prefix or []   # Result - []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M - 1, prefix)
        prefix.pop()


def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    for digit in '0', '1':
        gen_bin(M - 1, prefix+digit)
    # else:
    #     # gen_bin(M - 1, prefix + "0")
    #     # gen_bin(M - 1, prefix + "1")


def find(number, A):
    """
    Ищет х в списке А
    :param number: искомое число
    :param A: список
    :return: True/False
    """
    for x in A:
        if number == x:
            return True
    return False
    # flag = False
    # for x in A:
    #     if number == x:
    #         flag = True
    #         break
    # return flag

def generate_permutations(N:int, M:int=-1, prefix=None):
    """
    Генерация всех перестановок N чисел в M позициях,
    с префиксом prefix
    :param N: N-числе
    :param M: кол-во оставшихся позиций
    :param prefix: префикс
    :return:
    """
    M = N if M == -1 else M     # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix) # end=", ", sep="" - if u want
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

# # только для двоичной СС:
# gen_bin(5)
#
# # для произвольной СС:
# generate_number(3, 3)
# print('_'*10)
generate_permutations(3)