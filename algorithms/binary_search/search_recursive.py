# Recursive solution
# Function takes only four arguments that I don't really like


def binary_search_recursive(arr, item, low=0, high=-1):
    if not arr:  # handling empty list
        return -1
    if high == -1:  # handling first iteration
        high = len(arr) - 1

    if low >= high:  # handle where we've got single element while working
        return low if arr[low] == item else -1

    mid_index = (low + high) // 2

    if arr[mid_index] > item:
        return binary_search_recursive(arr, item, low, mid_index - 1)
    elif arr[mid_index] < item:
        return binary_search_recursive(arr, item, mid_index+1, high)
    else:
        return mid_index  # when we guess from first time


# General cases
assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], 5) == 4
assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], 4) == 3
assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2

# First and last elements of list
assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], 1) == 0
assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], 8) == 7

# Not found
assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], 0) == -1
assert binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], 11) == -1

# Empty list
assert binary_search_recursive([], 1) == -1

# With one element
assert binary_search_recursive([1], 1) == 0

assert binary_search_recursive([1, 2], 1) == 0
assert binary_search_recursive([1, 2], 2) == 1
