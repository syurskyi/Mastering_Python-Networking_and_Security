#!/usr/bin/python
__author__ = 'syurskyi'

class Me:
    def __init__(self, foo):
        self.myvar = foo

    def getval(self):
        return self.myvar


my = Me("this")
x = my.getval()
print(x)
