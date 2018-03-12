"""
Code was taken and combined from:

https://gist.github.com/jvashishtha/2720700
https://pythonandr.com/2015/07/05/the-merge-sort-python-code/
https://www.pythoncentral.io/merge-sort-implementation-guide/
"""


def merge_sort(alist):
    print("Splitting ", alist)

    if len(alist) > 1:
        mid = len(alist) // 2

        # Handle left side of list
        left_half = alist[:mid]
        merge_sort(left_half)

        # Handle right side of list
        right_half = alist[mid:]
        merge_sort(right_half)

        # #### Code goes down when right_half and left_half are one elements
        i = 0
        j = 0
        k = 0  # additional index for pointing to the  main list

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1

    print("Merging ", alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(alist)
print(alist)
