class InfiniteIterator:

    def __init__(self):
        self.__number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__number += 1
        return self.__number

# Just plain usage of InfiniteIterator
doubler = InfiniteIterator()
counter = 0
for number in doubler:
    # print(number)
    if counter > 10:
        break
    counter += 1


# Create iterable from InfiniteIterator
class InfiniteNumbers:
    def __iter__(self):
        return InfiniteIterator()

infinite_numbers = InfiniteNumbers()

for x in infinite_numbers:
    print(x)

    if x > 99:
        break
