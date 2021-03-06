import functools

"""Check function arguments for given type."""


def check(*argtypes):
    """
    Function argument type checker.
    """
    def _check(func):

        @functools.wraps(func)
        def __check(*args):
            """
            Takes the arguments
            """
            if len(args) != len(argtypes):
                msg = 'Expected %d but got %d arguments' % (
                    len(argtypes), len(args)
                )
                raise TypeError(msg)
            for arg, argtype in zip(args, argtypes):
                if not isinstance(arg, argtype):
                    msg = 'Expected %s but got %s' % (
                        argtypes, tuple(type(arg) for arg in args)
                    )
                    raise TypeError(msg)
            return func(*args)
        return __check
    return _check


@check(int, int)
def add(x, y):
    return x + y

print(add(2, 4))
print(add(2, 1))
print(add(2, '1'))
print(add(2, 3, 4))


