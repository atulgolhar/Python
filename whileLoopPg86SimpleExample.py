#!/usr/bin/env python3
# whileLoopPg86SimpleExample.py

name = ""

# addresses only two cases:
# pressing Enter or pressing spacebar(s) then Enter

while not name or name.isspace():  
    name = input('Please input your name: ')
print('Hello, {}!!!!'.format(name))
