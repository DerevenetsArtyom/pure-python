import collections
from pprint import pprint


class LoggingDict(dict):
    def __setitem__(self, key, value):
        print('Setting %r to %r' % (key, value))
        super().__setitem__(key, value)


class LoggingOD(LoggingDict, collections.OrderedDict):
    pass


pprint(LoggingOD.__mro__)
#  <class '__main__.LoggingOD'>,
#  <class '__main__.LoggingDict'>,
#  <class 'collections.OrderedDict'>,
#  <class 'dict'>,
#  <class 'object'>

"""
The MRO shown above is the one order that follows from those constraints:

* LoggingOD precedes its parents, LoggingDict and OrderedDict
* LoggingDict precedes OrderedDict because LoggingOD.__bases__ is (LoggingDict, OrderedDict)
* LoggingDict precedes its parent which is dict
* OrderedDict precedes its parent which is dict
* dict precedes its parent which is object

The process of solving those constraints is known as linearization. 
There are a number of good papers on the subject, but to create subclasses with 
an MRO to our liking, we only need to know the two constraints: 
children precede their parents and 
the order of appearance in __bases__ is respected.
"""