# Time Complexity of Solution:
# Best O(n); Average O(n^2); Worst O(n^2).
#
# Approach:
# Insertion sort is good for collections that are very small or nearly sorted.
# Otherwise it's not a good sorting algorithm:
# it moves data around too much.
# Each time an insertion is made, all elements in a greater position are shifted


def insertion_sort(arr):
    # since we want to swap an item with previous one, start from 1
    for i in range(1, len(arr)):

        # current_value will be used for comparison with previous items,
        # and sent to the place it belongs
        current_value = arr[i]

        # reducing i directly will mess loop, so reduce its 'position' instead
        position = i

        # position > 0 bcoz no point going till arr[0] since there is
        # no seat available on its left, for current_value

        while position > 0 and arr[position - 1] > current_value:
            # Move the bigger item one step right to make room for current_value
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value


alist = [5, 2, 1, 9, 0, 4, 6]
print('Before', alist)
insertion_sort(alist)
print('After ', alist)
