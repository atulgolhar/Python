#!/usr/bin/env python3
# Simple average, refactored code.

print("Type integer, each followed by Enter; or just ControlD to finish.")
total = 0
count = 0

while True:
    try:
        line = input("Integer input: ")
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break

if count:
    print("count = ", count, "total = ", total, "avg = ", total/count)
