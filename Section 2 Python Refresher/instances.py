#!/usr/bin/python
__author__ = 'syurskyi'


class Me:
    def __init__(self, foo):
        self.myvar = foo

    def getval(self):
        return self.myvar

    def setval(self, y):
        self.myvar = y


my1 = Me("this")
my2 = Me("who")
my3 = Me("self")
x = my1.getval()
print(x)
x = my2.getval()
print(x)
x = my3.getval()
print(x)
my3.setval("testing")
x = my3.getval()
print(x)

