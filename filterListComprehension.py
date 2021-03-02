#!/usr/bin/env python3
# filterListComprehension.py

>>> [x for x in seq if x.isalnum()]
['foo', 'x41']

>>> [x for x in seq2 if x.isalnum()]
['foo', 'x41', 'sdfs', '23424', 'grr']

>>> [x for x in seq3 if x.isalnum()]
['foo', 'x41', '789', 'sdfs', '23424', 'grr']
