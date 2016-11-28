#bigdigits.py 

#!/usr/bin/env python3

#Given a number on the command line, the program outputs the same number onto the console using "big" digits. 
#Execute: input digit 1 to 9 from cmd line for example:
python3 bigdigits.py 8

import sys

Zero = ["  **  ", " *  * ", "*    *", "*    *", "*    *", " *  * ", "  **  "]
One =  ["   * ", "  ** ", "   * ", "   * ", "   * ", "   * ", "  ***"]
Two =  [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three =[" ****", "    *", "    *", " ****", "    *", "    *", " ****"]
Four = ["*   *", "*   *", "*   *", "*****", "    *", "    *", "    *"]
Five = ["*****", "*    ","*    ", "*****", "    *", "    *", "*****"]
Six =  ["*    ", "*    ", "*    ", "*****", "*   *", "*   *", "*****"]
Seven =["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight =["*****", "*   *", "*   *", "*****", "*   *", "*   *", "*****"]
Nine = ["*****", "*   *", "*   *", "*****", "    *", "    *", "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            print("Check row column", row, column)
            line += digit[row] + "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
