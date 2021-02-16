#!usr/bin/env python
# formattedPriceList.py
# Print a formatted price list with a given width

width = int(input('Please enter width: '))                    #1

price_width = 10                                              #2
item_width = width - price_width                              #3

header_fmt = '{{:{}}} {{:>{}}}'.format(item_width, price_width)

item_fmt = '{{:{}}} {{:>{}.2f}}'.format(item_width, price_width)

print('=' * width)                                            #4
print(header_fmt.format('Item', 'Price'))                     #7 8

print('-' * width)                                            #5
print(item_fmt.format('Apples', 0.4))
print(item_fmt.format('Pears', 0.5))
print(item_fmt.format('Canaloupes', 1.92))
print(item_fmt.format('Dried Appricots (16 oz.)', 8))
print(item_fmt.format('Prunes (4 lbs.)', 12))
print('=' * width)                                            #6
