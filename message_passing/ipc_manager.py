#!/usr/bin/env python
# encoding: utf-8
'''
manager support:
listdict Namespace Lock RLock
Semaphore BoundedSemaphore Condition
Event Barrier Queue Value Array
 
Created on Aug 20, 2019
@author: siqi.zeng
@change: Aug 20, 2019 siqi.zeng: initialization

'''
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()
        print(d)
        print(l)