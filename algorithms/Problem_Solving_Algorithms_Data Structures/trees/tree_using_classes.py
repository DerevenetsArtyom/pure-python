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

