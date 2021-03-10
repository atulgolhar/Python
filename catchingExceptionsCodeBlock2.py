#!/usr/bin/env
# catchingExceptionsCodeBlock2.py

def CatchingExceptionsCodeBlock2():
    try:
        1/0
    except NameError:                       # notice NameError used this time
        print('Unknown variable 0 ZERO')
    else:
        print('That went well')
    finally:
        print('Cleaning up')
