""" Simple implementation of syntax parsing tree """


# Helper structure
class Stack:
    def __init__(self):
        self.lst = []

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def is_empty(self):
        return self.lst == []

    def size(self):
        return len(self.lst)


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        # links to another BinaryTree instances
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        binary_tree = self.__class__(new_node)  # create new instance of tree

        if self.left_child is None:
            self.left_child = binary_tree
        else:
            binary_tree.left_child = self.left_child  # move existing node
            self.left_child = binary_tree  # assign created tree as left child

    def insert_right(self, new_node):
        binary_tree = self.__class__(new_node)  # create new instance of tree

        if self.right_child is None:
            self.right_child = binary_tree
        else:
            binary_tree.right_child = self.right_child  # move existing node
            self.right_child = binary_tree  # assign created tree as right child

    def get_root_value(self):
        return self.root

    def set_root_value(self, new_val):
        self.root = new_val

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child


def build_parse_tree(expression: str):
    LEFT_BRACKET = '('
    RIGHT_BRACKET = ')'
    OPERATORS = ['+', '-', '*', '/']

    tokens_list = expression.split()
    stack = Stack()  # need stack to traverse tree, move up and down
    tree = BinaryTree('')

    stack.push(tree)
    current_tree = tree

    for token in tokens_list:
        if token == LEFT_BRACKET:
            current_tree.insert_left('')  # add new tree to left side
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif token.isdigit():
            current_tree.set_root_value(token)
            current_tree = stack.pop()  # move to the parent node
        elif token in OPERATORS:
            current_tree.set_root_value(token)
            current_tree.insert_right('')  # add new tree to right side
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif token == RIGHT_BRACKET:
            current_tree = stack.pop()
        else:
            raise ValueError

    return tree


pt = build_parse_tree("( ( 10 + 5 ) * 3 )")

print(pt.get_root_value())
print(pt.get_left_child().get_root_value())
print(pt.get_right_child().get_root_value())





