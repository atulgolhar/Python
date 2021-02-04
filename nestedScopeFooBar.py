#!/usr/bin/env python3
# NestedScopeFooBar.py

def foo():
    print('printed foo')
    user_name = input("What is your name? ")imp
    print("ok so your name is ", user_name, "!!!!")
    def bar():
        print('printed bar')
        print("Hello World!")
    bar()
