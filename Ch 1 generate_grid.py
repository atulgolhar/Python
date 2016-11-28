#!/usr/bin/env python3

#generategrid.py
#Generate a grid of random integers

import random

def get_int(msg, minimum, default):
  
#Function always returns either default (if user presses Enter) or a valid integer
#that is greater than or equal to the specified minimum

    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default                      #flow of control drops thru to next line
            i = int(line)
            if i < minimum:
                print("must be >=", minimum)
            else:
                return i 
        except ValueError as err:
            print("ValueError", err)

#user interaction
rows = get_int("rows: ", 1, None)
columns = get_int("columns: ", 1, None)
minimum = get_int("minimum (or Enter for 0): ", -1000000, 0)

default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int("maximum (or Enter for " + str(default) + "): ", minimum, default)

#processing - use 3 while loops to generate grid with outer loop (rows), middle loop (columns), 
#and inner loop (character spacing)
row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)        #obtain random number in specified range 
        s = str(i)
        while len(s) < 10:        #to pad string with leading spaces, set string at 10 charaters wide
            s = " " + s
        line += s                 #use line string to accumulate the numbers as strings for each row
        column += 1
    print(line)
    row += 1
