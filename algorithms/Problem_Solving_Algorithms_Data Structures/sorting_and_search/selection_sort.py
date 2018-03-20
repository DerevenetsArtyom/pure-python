def selection_sort_reverse_order(arr):
    """Sort the mutable sequence seq in place and return it."""
    for right_index in range(len(arr) - 1, 0, -1):
        index_of_max = 0
        # Find the index of greatest item in seq[:i+1]
        for i in range(1, right_index + 1):
            if arr[i] > arr[index_of_max]:
                index_of_max = i

        arr[right_index], arr[index_of_max] = \
            arr[index_of_max], arr[right_index]


def selection_sort_right_order(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort_reverse_order(alist)

assert alist == [17, 20, 26, 31, 44, 54, 55, 77, 93]


blist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort_right_order(blist)

assert blist == [17, 20, 26, 31, 44, 54, 55, 77, 93]
