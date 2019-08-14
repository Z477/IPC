#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Aug 13, 2019
@author: siqi.zeng
@change: Aug 13, 2019 siqi.zeng: initialization
'''

from multiprocessing import Process, Array

def fun(a, i):
    a[i] = -a[i]

def main():
    arr = Array('i', range(10))
    print("start {}".format(arr[:]))
    p_list = [Process(target=fun, args=(arr, i)) for i in range(10)]
    for p in p_list:
        p.start()
    for p in p_list:
        p.join()
    print("end {}".format(arr[:]))

if __name__ == '__main__':
    main()

