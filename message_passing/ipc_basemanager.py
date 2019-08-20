#!/usr/bin/env python
# encoding: utf-8
'''
Module Description

Created on Aug 20, 2019
@author: siqi.zeng
@change: Aug 20, 2019 siqi.zeng: initialization
'''

from multiprocessing.managers import BaseManager
from multiprocessing import Process
def server():
    manager = BaseManager(address=('127.0.0.1', 50000), authkey=b'abc')
    content = "hello"
    manager.register("get_words", callable=lambda: content)
    server = manager.get_server()
    server.serve_forever()

def client():
    m = BaseManager(address=('127.0.0.1', 50000), authkey=b'abc')
    m.register('get_words')
    m.connect()
    print(m.get_words())


def main():
    Process(target=server, args=()).start()
    Process(target=client, args=()).start()

if __name__ == "__main__":
    main()