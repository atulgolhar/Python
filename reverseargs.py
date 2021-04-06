# Reversing and Printing Command Line Arguments

# reverseargs.py
import sys
args = sys.argv[1:]     # make copy and skip first element
args.reverse()          # reverse the list
print(' '.join(args))   # not able to print an in-place modication thus created a copy

# Example
$ python reverseargs.py this is a test
test a is this
