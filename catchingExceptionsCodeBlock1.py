#!/usr/bin/env
# catchingExceptionsCodeBlock1.py

def CatchingExceptionsCodeBlock():
    while True:
        try:
            x = int(input('Enter the 1st number: '))
            y = int(input('Enter the 2nd number: '))
            print(x/y)
            print('Happy New Year! This works.')
        except Exception as e:
            print("Invalid input", e)
            print('Try again')
        else:
            print('Now Else break line triggered')
            break
            
