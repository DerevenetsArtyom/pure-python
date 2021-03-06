class BinaryHeap:
    """Min-heap"""
    root_index = 1

    def __init__(self):
        self.heap_list = [0]  # initial 0 is needed for correct division
        self.size = 0  # represents length minus first '0'

    def insert(self, item):
        """Add element to list and then move it to right position"""
        self.heap_list.append(item)
        self.size += 1
        self._move_up(self.size)

    def del_min(self) -> int:
        old_root = self.heap_list[self.root_index]
        last_element = self.heap_list.pop()

        # move last element to the top to support heap's structure property
        self.heap_list[self.root_index] = last_element
        self.size -= 1

        # restore property of orderliness,
        # cause it was broken by inserting new root
        self._move_down(self.root_index)

        return old_root

    def build_heap(self, _list):
        i = len(_list) // 2
        self.size = len(_list)  # +1 ???
        self.heap_list = [0] + _list[:]

        while i > 0:
            self._move_down(i)
            i -= 1

    def _move_up(self, i: int):
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

    def _move_down(self, i: int):
        """
        Swap root with smaller child while it won't be smaller than both childs
        """
        # i * 2     - represents index of left child
        # i * 2 + 1 - represents index of right child
        while (i * 2) <= self.size:
            # find index of min child (left or right child)
            min_child_indx = self._min_child(i)

            if self.heap_list[i] > self.heap_list[min_child_indx]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child_indx]
                self.heap_list[min_child_indx] = tmp
            i = min_child_indx

    def _min_child(self, i: int) -> int:
        left_ch_indx = i * 2
        right_ch_indx = i * 2 + 1

        if right_ch_indx > self.size:  # no right child
            return left_ch_indx
        else:
            # find smallest child and it's index
            if self.heap_list[left_ch_indx] < self.heap_list[right_ch_indx]:
                return left_ch_indx
            else:
                return right_ch_indx


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

bh2 = BinaryHeap()
bh2.build_heap([9, 6, 5, 2, 3])
print(bh2.heap_list)
