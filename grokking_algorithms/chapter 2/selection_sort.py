def findSmallest(arr):
    """
    Функция для поиска наименьшего элемента массива.
    :param arr: входной массив данных
    :return: индекс наименьшего элемента массива
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    """
    Функция осуществляет сортирку выбором.
    :param arr: входной массив данных
    :return: НОВЫЙ отсортированный массив
    """
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
