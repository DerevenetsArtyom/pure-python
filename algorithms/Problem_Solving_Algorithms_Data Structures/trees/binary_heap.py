class BinaryHeap:
    """Min-heap"""
    def __init__(self):
        self.heap_list = [0]  # initial 0 is needed for correct division
        self.size = 0  # length except first '0'

    def _move_up(self, i):
        """Takes last element and try to move it up"""
        while i // 2 > 0:
            current_elem = self.heap_list[i]
            parent_elem = self.heap_list[i // 2]

            # keep small elements as 'high' as possible
            if current_elem < parent_elem:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, item):
        """Add element to list and then move it to right position"""
        self.heap_list.append(item)
        self.size += 1
        self._move_up(self.size)

    def _min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def _move_down(self, i):
        """Чтобы поддержать свойство упорядоченности, надо поменять местами
        корень с меньшим, чем он, потомком.
        После начальной перестановки можно повторять процесс для узла и его
        потомков до тех пор, пока он не переместится на позицию,
        в которой будет меньше обоих своих детей"""
        while (i * 2) <= self.size:
            min_child_indx = self._min_child(i)
            if self.heap_list[i] > self.heap_list[min_child_indx]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child_indx]
                self.heap_list[min_child_indx] = tmp
            i = min_child_indx

    def del_min(self):
        old_root = self.heap_list[1]
        last_element = self.heap_list[-1]  # or self.heapList[self.currentSize]

        # move last element to the top to support heap's structure property
        self.heap_list[1] = last_element
        self.heap_list.pop()  # TODO assign to last element
        self.size -= 1

        # try to return property of orderliness, cause it broken
        self._move_down(1)
        return old_root


bh = BinaryHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)
bh.insert(2)
bh.insert(6)

print(bh.heap_list)

bh.del_min()
print(bh.heap_list)

bh.del_min()
print(bh.heap_list)
