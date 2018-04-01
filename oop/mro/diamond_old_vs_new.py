import sys


def mro_resolution():
    class A:
        x = 'a'

    class B(A):
        pass

    class C(A):
        x = 'c'

    class D(B, C):
        pass

    print(D.x)


if __name__ == '__main__':
    if sys.version_info.major == 2:
        print('Version #2. Old-style classes')
        print('  MRO: D - B - A - C - A (in-depth)')
        mro_resolution()  # 'a'

    if sys.version_info.major == 3:
        print('Version #3. New-style classes')
        print('  MRO: D -> B -> C -> A -> object')
        print()
        mro_resolution()  # 'c'
