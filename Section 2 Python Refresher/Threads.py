#!/usr/bin/python3
__author__ = 'syurskyi'

import threading


class AThread(threading.Thread):
    def __init__(self, num, val):
        threading.Thread.__init__(self)
        self.threadNum = num
        self.loopCount = val

    def run(self):
        print("Starting run: ", self.threadNum)
        myfunc(self.threadNum, self.loopCount)


def myfunc(num, val):
    count=0
    while count < val:
        print(num, " : ", val*count)
        count = count+1


t1=AThread(1, 15)
t2=AThread(2, 20)
t3=AThread(3, 25)
t4=AThread(4, 30)

#  have to start them
t1.start()
t2.start()
t3.start()
t4.start()

#  could join them all into a collection
#  so first define a collection
threads = []
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)

#  wait for all threads to complete by entering them
for t in threads:
    t.join()