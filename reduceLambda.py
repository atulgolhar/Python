# reduceLambda.py

>>> numbersA = [1,2,3,4,5,6,7,8]
>>> from functools import reduce
>>> reduce(lambda x, y: x+ y, numbersA)
36
>>> numbersB = [1,2,3,4,5]
>>> 1+2+3+4+5
15
>>> reduce(lambda x,y: x+y, numbersB)
15
>>> 
