# 1. Example with decorator with parameters
def smart_divide(func):
    def inner(a, b):
        print('I am going to divide {} and {}'.format(a, b))
        if b == 0:
            print('Whoops! Cannot divide')
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a / b

# print(divide(2, 5))
# print(divide(1, 5))
# print(divide(1, 0))


# 2. Chain  of decorators
def star(func):
    def inner(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print('%%%%%%%%%%')
        func(*args, **kwargs)
        print('%%%%%%%%%%')
    return inner


@star
@percent
def printer(msg):
    print(msg)
# This is the same as printer = star(percent(printer))

printer('Hello')


# 3. Another examples
def bold(func):
    def inner():
        return '<b>{}</b>'.format(func())
    inner.__name__ = func.__name__
    return inner


def emph(func):
    def inner():
        return '<em>{}</em>'.format(func())
    inner.__name__ = func.__name__
    return inner


@emph
@bold
def printer():
    return 'hello'

print(printer.__name__)
