#!/usr/bin/env python
# IndexingDate_mvp.py

# Prints out a date, given user input of year, month, and day as numbers.

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December']

year = input('Year 4 digits: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')

print(month + '-' + day + '-' + year)
