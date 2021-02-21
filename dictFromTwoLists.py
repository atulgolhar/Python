#!/usr/bin/env python3
# dictFromTwoLists.py

# creating dictionary from two lists

names = ['Alice', 'Beth', 'Cecil', 'Dee', 'Earl']
numbers = ['1234', '3652', '8526', '9834', '2355']

numbers[names.index('Cecil')]       # '8526'
names[2]                            # 'Cecil'
numbers[2]                          # '8526'
numbers[names.index('Cecil')]       # '8526'

"""
>>> numbers
[]
>>> numbers = ['1234', '3652', '8526', '9834', '2355']
>>> test_keys
['Alice', 'Beth', 'Cecil', 'Dee', 'Earl']
>>> test_values
[]
>>> test_values = numbers
"""


TRY 1 - Method 1 - Naive 
>>> test_keys = names
>>> test_values = numbers
>>> resultdict1 = {}
>>> for key in test_keys:
    for value in test_values:
        resultdict1[key] = value
        test_values.remove(value)
        break
>>> print(resultdict1)
{'Alice': '1234', 'Beth': '3652', 'Cecil': '8526', 'Dee': '9834', 'Earl': '2355'}


TRY 2 - Method 2 - condense code
>>> resultdict2 = {test_keys[i] : test_values[i] for i in range(len(test_keys))}
>>> print(resultdict2)
{'Alice': '1234', 'Beth': '3652', 'Cecil': '8526', 'Dee': '9834', 'Earl': '2355'}


TRY 3 - Dictionary zip() method
>>> resultdict3 = dict(zip(test_keys, test_values))
>>> print(resultdict3)
{'Alice': '1234', 'Beth': '3652', 'Cecil': '8526', 'Dee': '9834', 'Earl': '2355'}
