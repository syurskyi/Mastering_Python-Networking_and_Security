#!/usr/bin/python3
__author__ = 'syurskyi'

import os
from subprocess import call

#  use the os interface to get access to system information
print(os.getcwd())
print(os.getuid())
print(os.getenv("PATH"))

# using system
os.system("ls -la")
# can use call
inp=input("Hit enter")
call(["ls", "-la"])


