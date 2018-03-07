# Iterative solution
# Function takes only two arguments that I mostly prefer


def binary_search_iterative(arr, item):
    """Array should be sorted!!!"""
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid_index = (first + last) // 2
        if item < arr[mid_index]:
            last = mid_index - 1
        elif item > arr[mid_index]:
            first = mid_index + 1
        else:
            return mid_index

    return -1


# General cases
assert binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8], 5) == 4
assert binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2

# First and last elements of list
assert binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8], 1) == 0
assert binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8], 8) == 7

# Not found
assert binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8], 0) == -1

# Empty list
assert binary_search_iterative([], 1) == -1

# With one element
assert binary_search_iterative([1], 1) == 0

assert binary_search_iterative([1, 2], 1) == 0
assert binary_search_iterative([1, 2], 2) == 1
