#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Aug 13, 2019
@author: siqi.zeng
@change: Aug 13, 2019 siqi.zeng: initialization
'''

from multiprocessing import Barrier,Process
import time
import os

def f(barrier, sleep_time):
    pid = os.getpid()
    print("start {} {}".format(pid, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
    time.sleep(sleep_time)
    print("start wait other process")
    barrier.wait()
    print("all process comes {} {} ".format(pid, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))

def main():
    barr = Barrier(2)
    Process(name='p1 - test_with_barrier', target=f, args=(barr, 1)).start()
    Process(name='p1 - test_with_barrier', target=f, args=(barr, 3)).start()

if __name__ == '__main__':
    main()