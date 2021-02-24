#!/usr/bin/env python3
# fibonacciBasic.py

fibs = [0,1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])

print(fibs)
print(len(fibs))
