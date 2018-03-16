class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]  # initial 0 is needed for correct division
        self.size = 0

    def _move_up(self, i):
        while i // 2 > 0:
            current_elem = self.heap_list[i]
            parent_elem = self.heap_list[i // 2]
            if current_elem < parent_elem:
                # current_elem, parent_elem = parent_elem, current_elem
                # parent_elem, current_elem = current_elem, parent_elem
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, item):
        self.heap_list.append(item)
        self.size += 1
        self._move_up(self.size)


bh = BinaryHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)

print(bh.heap_list)





















# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
