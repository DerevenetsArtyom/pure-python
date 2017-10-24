def decorator(arg1, arg2):
    def inner_function(function):
        def wrapper(*args, **kwargs):
            print('Arguments passed to decorator {} and {}'.format(arg1, arg2))
            function(*args, **kwargs)

        return wrapper

    return inner_function


@decorator('foo', 'bar')
def print_args(*args):
    for a in args:
        print(a)

print_args(1, 2, 4, 5, 6, 6, 7)
