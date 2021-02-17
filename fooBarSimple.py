#!/usr/bin/env python3
# fooBarSimple.py
# executing simple nested method call example

def foo():
    print('printed foo')
    def bar():
        print('printed bar')
        print("Hello World!")
    bar()
    
