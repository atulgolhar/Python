#!/usr/bin/env python3
# nestingBlocksExample.py

# simple example, Chapter 5, pg 79
# ask user for one name only and
# try to determine is its a Mr, Mrs, or kid


name = input('What is your name? ')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print('Hello, Mr. Gumby')
    elif name.startswith('Mrs.'):
        print('Hello, Mrs. Gumby')
    else:
        print('Hello kid Gumby')
else:
        print('hello stranager')
