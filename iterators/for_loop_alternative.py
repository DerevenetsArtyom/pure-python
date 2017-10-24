l = [1, 2, 3, 4, 5]

iterator = iter(l)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        print('this is the end')
        break

