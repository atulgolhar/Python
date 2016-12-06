#!/usr/bin/env python3
#fibonacci.py
#multiple methods to execute fibonacci (interpreter vs command line)

def fib1(n):
  a, b = 0, 1
  while b < n:
    print(b, end=' ')
    a, b = b, a+b
  print()

def fib2(n):
  result = []
  a, b = 0, 1
  while b < n:
    result.append(b)
    a, b = b, a+b
  print()
  return result

if __name__ == "__main__":
  import sys
  fib1(int(sys.argv[1]))
