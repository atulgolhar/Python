#!/usr/bin/env python3
# recursionExponents.py

# Approach #2 - use recursion
# base case x to the power 0 always = 1
#       thus power(x,0) is 1 for all numbers x
# 
>>> 
>>> def power(x,n):
        if n == 0:
            return 1
        else:
            return x * power(x,n-1)
    
>>> power(2,4)
16
>>> power(2,3)
8

# selfcheck included
>>> def powerA(x,n):
        if n == 0:
            print('base:',x,n,n-1)
            return 1
        else:
            print('recursion:',x,n,n-1)
            return x * powerA(x,n-1)
    
>>> powerA(2,3)
recursion: 2 3 2
recursion: 2 2 1
recursion: 2 1 0
base: 2 0 -1
8
