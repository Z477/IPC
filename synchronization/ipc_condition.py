#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Aug 13, 2019
@author: siqi.zeng
@change: Aug 13, 2019 siqi.zeng: initialization
'''

from multiprocessing import Process, Condition, Value
import time
import os


def producer(count, con):
    while True:
        if con.acquire():
            count.value += 10
            msg = str(os.getpid()) + ' produce 10, count=' + str(count.value)
            print(msg)
            #notify all thread which wait the condition
            con.notify_all()
            con.release()
        time.sleep(1)


def consumer(count, con):
    while True:
        #acquire for the lock
        if con.acquire():
            while count.value == 0:
                #release the lock when wait, after be notified, will return a lock
                con.wait()
            count.value -= 1
            msg = str(os.getpid()) + ' consume 1, count=' + str(count.value)
            print(msg)

            con.release()

def test():
    count = Value('i', 0)
    con = Condition()
    for i in range(2):
        Process(target=producer, args=(count, con)).start()

    for i in range(5):
        Process(target=consumer, args=(count, con)).start()

if __name__ == '__main__':
    test()