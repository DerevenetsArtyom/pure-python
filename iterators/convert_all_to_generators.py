"""
Not much of a difference at first sight, but the benefits are pretty substantial
* No bookkeeping.
    You don't have to create an empty list, append to it, and return it.
    One more variable gone.
* Hardly consumes memory.
    No matter how large the input file is,
    the iterator version does not need to buffer the entire file in memory;
* Works with infinite streams.
    The iterator version still works if f is an infinite stream;
* Faster results.
    Results can be consumed immediately, not after the entire file is read;
* Speed.
    The iterator version runs faster than building a list the naive way;
* Composability
    The caller gets to decide how it wants to use the result.
"""
some_list = []


# Simple stupid function
def get_numbers_stupid(l):
    res = []
    for i in l:
        if i % 2 == 0:
            res.append(i)
    return res

numbers = get_numbers_stupid(some_list)


# Function, using generator
def get_numbers_gen(l):
    for i in l:
        if i % 2 == 0:
            yield i

new_numbers = list(get_numbers_gen(some_list))
