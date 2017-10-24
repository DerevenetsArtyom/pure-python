import functools


# Decorators Without Arguments
def decorator(function):
    @functools.wraps(function)
    def _wrapper(*args, **kwargs):
        # do smth before function call
        result = function(*args, **kwargs)
        # do smth after function call
        return result

    # Without @functools.wraps(function)
    # _wrapper = functools.wraps(function)(_wrapper)
    return _wrapper


# Decorators With Arguments
def arguments_decorator(arg1, arg2):
    def outer_wrapper(function):
        def _wrapper():
            # do smth before function call
            result = function()
            # do smth after function call
            return result * arg1 * arg2
        return _wrapper
    return outer_wrapper

##################################################################


def p_decor(func):
    @functools.wraps(func)
    def inner(name):
        return '<p>{}</p>'.format(func(name))
    return inner


@p_decor
def get_text(name):
    return 'The name is {}'.format(name)
# text_with_p = p_decor(get_text)

print(get_text('hi there'))
























