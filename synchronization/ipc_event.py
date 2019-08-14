#!/usr/bin/env python
# encoding: utf-8
'''
Module Description

Created on Aug 13, 2019
@author: siqi.zeng
@change: Aug 13, 2019 siqi.zeng: initialization
'''

from multiprocessing import Process, Event
import time
import os

def f(e):
    pid = os.getpid()
    print("start pid: {}, e.is_set={}, {}".format(pid, e.is_set(), time.strftime("%Y-%m-%d %H:%M:%S",  time.localtime())))
    if e.wait(2):
        print("end pid: {}, e.is_set={}, {}".format(pid, e.is_set(), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


def main():
    e = Event()
    for _ in range(3):
        Process(target=f, args=(e,)).start()
    time.sleep(1)
    e.set()

if __name__ == '__main__':
    main()