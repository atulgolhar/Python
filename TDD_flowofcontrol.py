#!/usr/bin/env python3
#Test Driven Development - Flow of Control Check

def get_int(arguments):
    print("Check2: ", arguments, type(arguments))
    while True:
        try:
            i = int(input(arguments)), print("Check3", arguments)
            print("Check4: ", arguments, type(arguments))
            print("Check5: ", i, type(i))
            return i
        except ValueError as err:
            print("Check6", type(err), err)

print("Flow of control check\n")
age = get_int("Check1: enter your age: ")

print("Check7: ", type(age), age)
