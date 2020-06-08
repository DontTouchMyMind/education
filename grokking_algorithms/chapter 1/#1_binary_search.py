def binary_search(input_list: list, item: int):
    """
    Функция получает отсортированный массив и значение,
    которое необходимо найти. Если значение присутствует,
    то функция возвращает его позицию.
    :param input_list: Отсортированный массив
    :param item: искомый элемент
    :return: индекс элемнта в массиве
    """
    low = 0
    high = len(input_list)
    while low <= high:
        mid = (low + high) // 2
        guess = input_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 2))
print(binary_search(my_list, 11))
