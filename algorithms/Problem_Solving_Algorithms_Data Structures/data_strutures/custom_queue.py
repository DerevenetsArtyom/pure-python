class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        # return self.items == []
        return not bool(self.items)

    def size(self):
        return len(self.items)


s = Queue()

assert s.isEmpty() is True
s.enqueue(4)
s.enqueue('dog')
s.enqueue(True)
assert s.size() == 3
assert s.isEmpty() is False
s.enqueue(8.4)
assert s.dequeue() == 4
assert s.dequeue() == 'dog'
assert s.size() == 2
