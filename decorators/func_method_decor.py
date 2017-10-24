import functools


def metod_decorator(method):
    def inner(city_instance):
        if city_instance.name == 'SFO':
            print('this is a cool place to live in')
        else:
            method(city_instance)
    return inner


class City:

    def __init__(self, name):
        self.name = name

    @metod_decorator
    def print_name(self):
        print(self.name)


c1 = City('SFO')
c2 = City('Plain city')

c1.print_name()
c2.print_name()
