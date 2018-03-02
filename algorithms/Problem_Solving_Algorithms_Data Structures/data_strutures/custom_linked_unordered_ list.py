# There are several types of inked lists:
#    Singly-linked list
#    Doubly-linked list  (two references)
#    Circular list


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None


class UnorderedList:
    # append, insert, index, pop not implemented ((
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        """
        1) Create a new Node
        2) Set 'next' in that node to current head (first node) of list
        3) Make that node head of list
        Order of 2 and 3 is very important here
        """
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next

        return count

    def search(self, element):
        current_node = self.head

        while current_node:
            if current_node.data == element:
                return True
            else:
                current_node = current_node.next
        return False

    def remove(self, item):
        current = self.head
        prev = None
        found = False

        while not found and current:
            if current.data == item:
                found = True
            else:
                prev, current = current, current.next

        if found is False:  # didn't find element - no need to move smth
            return

        if prev is None:  # we are in the very first node
            self.head = current.next
        else:
            prev.next = current.next


lst = UnorderedList()
lst.add(1)
lst.add(2)
lst.add(3)
lst.add(4)
lst.add(5)

assert lst.size() == 5

assert lst.search(1) is True
assert lst.search(2) is True
assert lst.search(3) is True
assert lst.search(4) is True
assert lst.search(5) is True
assert lst.search(55) is False
assert lst.search(51) is False

lst.remove(34)
assert lst.size() == 5

lst.remove(5)
assert lst.size() == 4
assert lst.head.data == 4

lst.remove(1)
assert lst.size() == 3
assert lst.search(1) is False


