#!/usr/bin/env python3
# nestingBlocks.py

# simple example, Chapter 5, pg 79
# ask user for one name only and
# try to determine is its a Mr, Mrs, or kid


name = input('What is your name? ')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print('Hello, Mr. Gumby')       # two conditions to get here
    elif name.startswith('Mrs.'):
        print('Hello, Mrs. Gumby')      # two conditions to get here
    else:
        print('Hello kid Gumby')        # only one condition to get here
else:
        print('hello stranager')        # no conditions

# note that error checking would make inputs more robust
# can enter R2D2, _______, #*$*#%, or any characters
