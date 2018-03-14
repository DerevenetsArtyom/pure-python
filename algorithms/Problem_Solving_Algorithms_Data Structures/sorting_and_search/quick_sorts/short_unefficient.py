def quicksort(arr):
    """
    Pretty slow and uneffective implementation,
    but here is fairly important trick:
    splitting array into three parts instead of two.
    So, for the input array with same items complexity will be better,
    while with two parts for that input it will be n^2 always.
    """
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    lowest = [x for x in arr if x < pivot]
    equals = [x for x in arr if x == pivot]
    greatest = [x for x in arr if x > pivot]

    return quicksort(lowest) + equals + quicksort(greatest)


list_ = [1, 4, 5, 6, 8, 33, 0, 10]
print(list_)
print(quicksort(list_))
print()

list_ = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(list_)
print(quicksort(list_))
print()

list_ = list(range(20, 0, -1))
print(list_)
print(quicksort(list_))
