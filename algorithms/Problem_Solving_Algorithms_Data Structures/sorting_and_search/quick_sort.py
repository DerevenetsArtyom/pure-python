# https://github.com/joeyajames/Python/blob/master/SortingAlgorithms.py#L108


def quick_sort(arr: list):
    # takes list itself, lower and highest indexes
    quick_sort_2(arr, 0, len(arr) - 1)


def quick_sort_2(arr: list, low: int, hi: int):
    # if more that one item is present
    if low < hi:
        # the most of work is doing in that function
        split_point = partition(arr, low, hi)  # pivot index

        quick_sort_2(arr, low, split_point)
        quick_sort_2(arr, split_point + 1, hi)


def partition(arr: list, low: int, hi: int) -> int:
    pivot_index = get_pivot(arr, low, hi)
    pivot_value = arr[pivot_index]

    # swap pivot value with very left value in list
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    border = low

    for i in range(low, hi + 1):
        if arr[i] < pivot_value:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]

    # swap border (very left value) with value "in the middle"
    arr[low], arr[border] = arr[border], arr[low]
    return border


def get_pivot(arr: list, low: int, hi: int) -> int:
    """Implementation getting pivot value by 'median of three' """
    mid_index = (low + hi) // 2
    sorted_values = sorted((arr[low], arr[mid_index], arr[hi]))

    # selecting middle value
    if sorted_values[1] == arr[low]:
        return low
    elif sorted_values[1] == arr[mid_index]:
        return mid_index
    return hi


list_ = [1, 4, 5, 6, 8, 33, 0, 10]
print(list_)
quick_sort(list_)
print(list_)
