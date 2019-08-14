#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Aug 12, 2019
@author: siqi.zeng
@change: Aug 12, 2019 siqi.zeng: initialization
'''
 
from multiprocessing import Pipe, Process
import os

def write(conn):
    content = "IPC"
    print("input {} to Pipe>> pid={}".format(content, os.getpid()))
    conn.send(content)
    conn.close()

def main():
    print("start parent process>>> pid={}".format(os.getpid()))
    conn1, conn2 = Pipe()
    p = Process(target=write, args=(conn2,))
    p.start()
    print("get {} from Pipe>>> pid={}".format(conn1.recv(), os.getpid()))
    p.join()

if __name__ == '__main__':
    main()