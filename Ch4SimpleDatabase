#!/usr/bin/env python

# a simple database example

people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },

    'Cecil': {
        'phone': '3158',
        'addr': 'Sunny lane 98'
    }
}

# descriptive labels for the phone number and address
# these will be used when printing the output
labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name: ')

# Are we looking for a phone number or address?
request = input('Phone number (p) or address (a)? ')

# use the correct key:
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# only try to print information if the name is a valid key
# in our dictionary

if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))
