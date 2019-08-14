#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Aug 13, 2019
@author: siqi.zeng
@change: Aug 13, 2019 siqi.zeng: initialization
'''
import redis
from multiprocessing import Process

def f1():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    while True:
        result = r.get("name")
        if result:
            print(result)

def f2():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    r.set('name', 'IPC')

def main():

    Process(target=f2, args=()).start()
    Process(target=f1, args=()).start()




if __name__ == '__main__':
    main()