#!/usr/bin/env python3

# fooNestedScopeMultiplier.py
# Example of nested funtions returning factor vs number

def multiplier(factor):
    print("Multiplier(Factor) --> ", factor)
    def multiplyByFactor(number):
        print("multiplyByFactor(number) --> ", number)
        print("Number = Factor", factor == number)
        print("Number: ", number)
        print("Factor: ", factor)
        return number * factor 
    return multiplyByFactor
