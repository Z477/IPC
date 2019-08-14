#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Aug 12, 2019
@author: siqi.zeng
@change: Aug 12, 2019 siqi.zeng: initialization
'''

import socket
from multiprocessing import Process


def server():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    print(host)
    s.bind((host, port))

    s.listen(5)
    while True:
        c, addr = s.accept()
        print(type(c))
        print(addr)
        c.send(b'hello')
        c.close()

def client():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.connect((host, port))
    print(s.recv(1024))
    s.close()

def main():
    Process(target=server, args=()).start()
    Process(target=client, args=()).start()


if __name__ == "__main__":
    main()