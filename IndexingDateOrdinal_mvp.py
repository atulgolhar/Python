#!/usr/bin/env python
# IndexingDateOrdinal_mvp.py

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
    'Novembe',
    'December']

year = input('Year 4 digits: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')

day_number = int(day)
month_number = int(month)
year_number = int(year)

print("String version")
print(month + '-' + day + '-' + year)
# need to expand code and explain this
print("Ordinal version")            
print(month_number, ' - ', day_number, ' - ', year_number)





#
