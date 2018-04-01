from pprint import pprint


class A:
    def x(self): print("A")


class B(A): pass


class C:
    def x(self): print("C")


class D(B, C): pass


instance = D()
instance.x()
# >>> A

pprint(D.__mro__)
# >>>
#  <class '__main__.D'>,
#  <class '__main__.B'>,
#  <class '__main__.A'>,
#  <class '__main__.C'>,
#  <class 'object'>

#      O
#     /|
#    A |
#   /  |
#  B   C
#  \   /
#    D
