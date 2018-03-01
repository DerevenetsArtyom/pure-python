class Stack:
    def __init__(self):
        self.lst = []

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def isEmpty(self):
        # return self.items == []
        return not bool(self.lst)

    def size(self):
        return len(self.lst)


s = Stack()

assert s.isEmpty() is True
s.push(4)
s.push('dog')

assert s.peek() == 'dog'
s.push(True)
assert s.size() == 3
assert s.isEmpty() is False
s.push(8.4)
assert s.pop() == 8.4
assert s.pop() is True
assert s.size() == 2
