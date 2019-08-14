#!/usr/bin/env python
# encoding: utf-8
'''
Queue demo
 
Created on Aug 12, 2019
@author: siqi.zeng
@change: Aug 12, 2019 siqi.zeng: initialization
'''
from multiprocessing import Queue, Process
import os
from time import sleep

def write(q):
    content = "IPC"
    print("input {} to Queue>> pid={}".format(content, os.getpid()))
    q.put(content)

def main():
    print("start parent process>>> pid={}".format(os.getpid()))
    q = Queue()
    p = Process(target=write, args=(q,))
    p.start()
    print("get {} from Queue>>> pid={}".format(q.get(), os.getpid()))
    p.join()


if __name__ == '__main__':
    main()