""" Simple implementation of syntax parsing tree """
import operator


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


def build_parse_tree(expression: str) -> BinaryTree:
    LEFT_BRACKET = '('
    RIGHT_BRACKET = ')'
    OPERATORS = ('+', '-', '*', '/', )

    # Stack as a list is needed to traverse the tree:
    #   .append (~.push) -> 'move down (deeper)' to the tree
    #   .pop -> 'move up' to the tree
    stack = list()
    tree = BinaryTree('')

    stack.append(tree)
    current_tree = tree
    tokens_list = expression.split()

    for token in tokens_list:
        if token == LEFT_BRACKET:
            current_tree.insert_left('')  # add new node to left side
            stack.append(current_tree)
            current_tree = current_tree.left_child

        elif token.isdigit():
            current_tree.root = int(token)
            current_tree = stack.pop()  # move 'up', to the parent node

        elif token in OPERATORS:
            current_tree.root = token
            current_tree.insert_right('')  # add new tree to right side
            stack.append(current_tree)
            current_tree = current_tree.right_child

        elif token == RIGHT_BRACKET:
            current_tree = stack.pop()

        else:
            raise ValueError
    return tree


def evaluate(parse_tree: BinaryTree) -> int:
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    left_child = parse_tree.left_child
    right_child = parse_tree.right_child
    root = parse_tree.root

    if left_child and right_child:
        operat_str = root  # should be operator as string
        operat_func = operators[operat_str]
        return operat_func(evaluate(left_child), evaluate(right_child))
    else:
        return root


if __name__ == '__main__':
    expr1 = "( ( 10 + 5 ) * 3 )"
    expr2 = "( 3 + ( 4 * 5 ) )"

    print(expr1)
    pt = build_parse_tree(expr1)
    print(evaluate(pt))
    print()

    print(expr2)
    pt = build_parse_tree(expr2)
    print(evaluate(pt))
