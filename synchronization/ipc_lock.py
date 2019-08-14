#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Aug 13, 2019
@author: siqi.zeng
@change: Aug 13, 2019 siqi.zeng: initialization
'''
from multiprocessing import Lock, Process
import os


def worker_with(lock, f):
    with lock:
        fs = open(f,"a+")
        fs.write('pid:{}\n'.format(os.getpid()))
        fs.close()

def main():
    f = "file.txt"

    lock = Lock()
    w = Process(target=worker_with, args=(lock, f))
    nw = Process(target=worker_with, args=(lock, f))

    w.start()
    nw.start()

    w.join()
    nw.join()


if __name__ == '__main__':
    main()
