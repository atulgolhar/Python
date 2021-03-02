#!/usr/bin/env python3
# filterFunctions.py


# BOX Throwing Functions Around (map, filter, reduce)    --> "ie Functional Programming = throwing functions around"
# pg 125
      # a few functions for "functional type" programming to create your own functions
      # map, filter are NOT that useful in current Python versions and 
      # thus use list comprehensions instead

map
# use map to pass all elements of a sequence though a given function
      >>> list(map(str, range(10)))
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
      >>> list(map(int, range(10)))
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      >>> 
      >>> listAstr = list(map(str, range(10)))
      >>> listAstr
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
      >>> listBint = list(map(int, range(10)))
      >>> listBint
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

filter 
# can filter out using a builtin method
# 

      >>> seq = ['foo','x41','?!','***']
      >>> def func(x):
              return x.isalnum()

      >>> list(filter(func, seq))
      ['foo', 'x41']
      >>> 

      >>> def func1(x):
              return x.isalnum()

      >>> list(filter(func1, seq))
      ['foo', 'x41']
      >>> 

      >>> def func2(x):
              return x.isnumeric()

      >>> list(filter(func2, seq))
      []

      >>> seq2 = ['foo','x41','?!','***', 'sdfs','23424','#$%fe','{{::','grr']

      >>> list(filter(func2, seq2))
      ['23424']


      >>> def func3(x):
                temp = '9'
                return x.endswith(temp)

      >>> seq3 = ['foo','x41','789','***', 'sdfs','23424','#$%fe','{{::','grr']

      >>> list(filter(func3, seq3))
      ['789']
      >>> 

