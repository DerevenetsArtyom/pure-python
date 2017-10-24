from itertools import islice


def fib():
    prev, cur = 0, 1
    while True:
        yield cur
        prev, cur = cur, cur + prev

f = fib()
print(list(islice(f, 0, 10)))

# Now when f = fib() is called, the generator is instantiated and returned.
# No code will be executed at this point:
#   the generator starts in an idle state initially.
# To be explicit: the line prev, curr = 0, 1 is not executed yet.
