# Reversing and Printing Command Line Arguments

# reverseargs.py
import sys
args = sys.argv[1:]
args.reverse()
print(' '.join(args))

$ python reverseargs.py this is a test
test a is this
