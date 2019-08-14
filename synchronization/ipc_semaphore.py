#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Aug 13, 2019
@author: siqi.zeng
@change: Aug 13, 2019 siqi.zeng: initialization
'''
from multiprocessing import Semaphore, Process

import os
import time


def func(semaphore):
    if semaphore.acquire():
        print("start pid: {} {} ".format(os.getpid(), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        time.sleep(2)
        semaphore.release()
        print("end pid: {} {}".format(os.getpid(),time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


def main():

    semaphore = Semaphore(3)
    for _ in range(6):
        Process(target=func, args=(semaphore,)).start()


if __name__ == '__main__':
    main()