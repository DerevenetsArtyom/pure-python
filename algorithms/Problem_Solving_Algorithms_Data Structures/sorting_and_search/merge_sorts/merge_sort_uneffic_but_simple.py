# https://stackoverflow.com/questions/18761766/mergesort-python

"""
You should not pop from lists, as that will shift elements over and over.
You should avoid changing the list anyway when iterating over it.


For the recursive calls you can use a helper function to which you
pass not sublists, but indices into x.
And the bottom level calls read their values from x and write into result directly.

That way you can avoid all that poping and appending which should improve performance.
"""


def merge_sort(x):
    if len(x) < 2:
        return x

    result, mid = [], len(x) // 2

    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])

    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z.pop(0))
        else:
            result.append(y.pop(0))

    result.extend(y + z)
    return result
