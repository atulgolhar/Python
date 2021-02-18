#!/usr/bin/env python
# getMethodExample.py 

# simple database using get()

people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'},
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'},
    'Cecil': {
        'phone': '3158',
        'addr': 'Sunny lane 98'}
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name: ')
request = input('Phone number (p) or address (a)? ')

# use correct key
key = request   # in case, neither 'p' nor 'a' is inputted
if request == 'p': key = 'phone'
if request == 'a': key = 'addr' 


# use get method to provide default values to catch error:
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

# if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))
print("{}'s {} is {}.".format(name, label, result))
