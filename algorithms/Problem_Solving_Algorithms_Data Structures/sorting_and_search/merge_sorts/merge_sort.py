"""
Code was taken and combined from:

http://rextester.com/PEAA86258
https://brilliant.org/wiki/merge/
https://gist.github.com/jvashishtha/2720700
https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort
https://codereview.stackexchange.com/questions/154135/recursive-merge-sort-in-python
"""

# The merge sort algorithm comes in two parts:
# * sort function
# * merge function


def merge(left, right):
    result = []
    left_idx = right_inx = 0
    # looping while exhaust one of arrays
    # P.S. change direction of comparison to change the direction of sort
    while left_idx < len(left) and right_inx < len(right):
        if left[left_idx] < right[right_inx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_inx])
            right_inx += 1

    # here we have reached end of left / right
    # and add to result rest of another list
    if left_idx < len(left):
        result.extend(left[left_idx:])

    if right_inx < len(right):
        result.extend(right[right_inx:])

    # Also could be without checking
    # result += left[left_index:]
    # result += right[right_index:]

    return result


def merge_sort(arr):
    """Divide array in half and merge sort recursively"""
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


alist = [5, 2, 1, 9, 0, 4, 6]
print(alist)

res = merge_sort(alist)
print('')
print(res)
