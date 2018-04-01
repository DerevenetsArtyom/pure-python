def meta_function(name, bases, attrs):
    print('Calling meta_function')
    return type(name, bases, attrs)


class MyClass1(metaclass=meta_function):
    def __new__(cls, *args, **kwargs):
        """
        Called to create a new instance of class `cls`.
        __new__ takes the class of which an instance was requested
        as its first argument.
        The remaining arguments are those passed to the object constructor
        expression (the call to the class).
        The return value of __new__ should be the
        new object instance (usually an instance of cls).
        """
        print('MyClass1.__new__({}, *{}, **{})'.format(cls, args, kwargs))
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        """
        Called after the instance has been created (by __new__),
        but before it is returned to the caller.
        The arguments are those passed to the object constructor.
        Note: both __new__ and __init__ receive the same arguments.
        """
        print('MyClass1.__init__({}, *{}, **{})'.format(self, args, kwargs))


a = MyClass1(1, 2, 3, x='ex', y='why')
