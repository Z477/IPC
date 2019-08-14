#!/usr/bin/env python
# encoding: utf-8
'''
Module Description
 
Created on Aug 13, 2019
@author: siqi.zeng
@change: Aug 13, 2019 siqi.zeng: initialization
'''

import xmlrpc.client
import xmlrpc.server
from multiprocessing import Process

def get_power(n,m):
    return n**m

def server():
    server = xmlrpc.server.SimpleXMLRPCServer(("0.0.0.0", 8081))
    print("start service get power on 0.0.0.0 8081...")
    server.register_function(get_power, "get_power")
    server.serve_forever()

def client():
    server_power = xmlrpc.client.ServerProxy("http://localhost:8081/")
    print("3**2 = %d" %(server_power.get_power(3,2)))
    print("2**5 = %d" %(server_power.get_power(2,5)))

def main():
    Process(target=server, args=()).start()
    Process(target=client, args=()).start()

if __name__ == "__main__":
    main()