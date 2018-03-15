"""
В дереве, представленном как список списков, на первой позиции мы будем хранить
значение корневого узла.
Второй элемент сам по себе будет списком и представит левое поддерево.
Третий элемент станет правым поддеревом.

Можно получить доступ к его корню, правому и левому поддеревьям.
Структура списка, представляющего поддерево, твёрдо придерживается определения
дерева - она рекурсивна сама по себе!
У поддерева есть корень и два пустых списка в качестве листьев.

Список списков легко расширяется до дерева, имеющего много поддеревьев -
когда дерево не является двоичным, новое поддерево - это новый подсписок.
"""

myTree = [
    'a',  # root -> myTree[0]
    ['b', ['d', [], []], ['e', [], []]],  # left subtree -> myTree[1]
    ['c', ['f', [], []], []]  # right subtree -> myTree[2]
]


#########################


def BinaryTree(root):
    """Just created a list out of input 'root' and two empty subtrees"""
    return [root, [], []]


def insert_left(root, new_branch):
    """
    Добавление к корню левого поддерева - вставить на 2-ую позицию новый список.

    Прежде, чем вставлять что-либо, мы получаем (возможно пустой) список,
    связанный с текущим левым потомком.

    Если на второй позиции уже что-то имеется, нужно сдвинуть элемент вниз
    по дереву, как левого потомка добавляемого списка.
    """
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_value(root):
    return root[0]


def set_root_value(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


r = BinaryTree(3)
insert_left(r, 4)
insert_left(r, 5)

insert_right(r, 6)
insert_right(r, 7)

lch = get_left_child(r)
rch = get_right_child(r)

assert lch == [5, [4, [], []], []]
assert rch == [7, [], [6, [], []]]

set_root_value(lch, 9)
print(r)
