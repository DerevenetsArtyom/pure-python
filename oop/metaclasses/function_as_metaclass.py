import re


def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def camel_to_snake_case(name, bases, attrs):
    """
    Metaclass will automatically get passed the same arguments
    that passed to `type`.
    Return a class object, with its attributes from camelCase to snake_case
    """
    print("Calling the metaclass 'camel_to_snake_case' to construct class:",
          name)

    print('Keys before:', [key for key in attrs if not key.startswith('__')])

    # pick up any attribute that doesn't start with '__' and snakecase it
    snake_attrs = {}
    for attr_name, attr_value in attrs.items():
        if not attr_name.startswith('__'):
            snake_attrs[convert(attr_name)] = attr_value
        else:
            snake_attrs[attr_name] = attr_value  # it's like internal attributes

    print('Keys after:', [key for key in snake_attrs if not key.startswith('__')])
    print()
    return type(name, bases, snake_attrs)  # let `type` do the class creation


class MyVector(metaclass=camel_to_snake_case):
    def addToVector(self, other): pass

    def subtractFromVector(self, other): pass

    def calculateDotProduct(self, other): pass

    def calculateCrossProduct(self, other): pass

    def calculateTripleProduct(self, other): pass


print([a for a in dir(MyVector) if not a.startswith('__')])