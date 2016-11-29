#!/usr/bin/env python3 

#average1_ans.py
#Simple calculator prompts user to enter a number using while loop. Gradually build up list.
#When finished press Enter, print out numbers, count, sum, lowest, highest and mean.

numbers = []
total = 0
lowest, highest = None, None

while True:
    try:
        line = input("Enter a number or Enter to finish: ")
        if not line: 
            break
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)
if numbers:
    print("\nAll Numbers Used: ", numbers, 
        "\nCount: ", len(numbers), "\nSum: ", total,
        "\nLowest: ", lowest, "\nHighest: ", highest,
        "\nMean: ", total / len(numbers))
