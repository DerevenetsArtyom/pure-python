def bubble_sort(arr):
    """
    Вне зависимости от первоначального порядка элементов,
    для списка из n элементов будет сделан n−1 проход
    """
    # reduce number of elements in every next iteration with shifting
    # right bound, but that doesn't reduce complexity (((
    for right_bound in range(len(arr) - 1, 0, -1):
        for i in range(right_bound):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


lst = [11, 1, 3, 4, 2, 66, 8]
bubble_sort(lst)
assert lst == [1, 2, 3, 4, 8, 11, 66]

"""
Однако, поскольку пузырьковая сортировка делает проход по всей несортированной 
части списка, она умеет то, что не могут большинство сортировочных алгоритмов. 
В частности, если во время прохода не было сделано ни одной перестановки, 
то мы знаем, что список уже отсортирован. 
Таким образом, алгоритм может быть модифицирован, чтобы останавливаться раньше, 
если обнаруживает, что задача выполнена. 
Т.е. для списков, которым нужно всего несколько проходов, пузырьковая сортировка
имеет преимущество, поскольку умеет распознать сортированный список 
и остановиться. 
Эту модификацию, которую часто называют коротким пузырьком.
"""


def short_bubble_sort(arr):
    exchanges = True  # keep track of made exchanges
    right_bound = len(arr) - 1
    while right_bound > 0 and exchanges:
        exchanges = False  # hope that elements will not exchange
        for i in range(right_bound):
            if arr[i] > arr[i + 1]:
                exchanges = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        right_bound -= 1


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(alist)
assert alist == [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
