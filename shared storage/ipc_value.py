#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Aug 13, 2019
@author: siqi.zeng
@change: Aug 13, 2019 siqi.zeng: initialization
'''
import time
from multiprocessing import Value,Process

def fun(val):
    val.value += 1

def mani():
    v = Value('i', 0)
    p_list = [Process(target=fun, args=(v,)) for i in range(10)]
    for p in p_list:
        p.start()
    for p in p_list:
        p.join()
    print(v.value)

if __name__ == '__main__':
    mani()