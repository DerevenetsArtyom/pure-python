#  Time Complexity of Solution:
#  Best O(n); Average O(n^2); Worst O(n^2).
#
#  Approach:
#  Insertion sort is good for collections that are very small
#  or nearly sorted. Otherwise it's not a good sorting algorithm:
#  it moves data around too much. Each time an insertion is made,
#  all elements in a greater position are shifted.

# https://www.geeksforgeeks.org/insertion-sort/
# https://codereview.stackexchange.com/questions/139056/insertion-sort-in-python
# https://stackoverflow.com/questions/12755568/how-does-python-insertion-sort-work


def insertion_sort(arr):
    for i in range(1, len(arr)):

        # element to be compared
        current_value = arr[i]

        position = i
        # comparing the current element with the sorted portion and swapping
        while position > 0 and current_value < arr[position - 1]:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value


alist = [5, 2, 1, 9, 0, 4, 6]
insertion_sort(alist)
print(alist)
