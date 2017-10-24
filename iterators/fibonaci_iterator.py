class Fib:
    def __init__(self):
        self.prev = 0
        self.current = 1

    def __iter__(self):
        print('__iter__', self)
        return self

    def __next__(self):
        print('__next__')
        value = self.current
        self.current += self.prev
        self.prev = value
        return value

f = Fib()
x = 1
while x < 10:
    print(next(f))
    x += 1
