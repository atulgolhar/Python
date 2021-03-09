# exceptionsClausev2.py
# So now I added more than one except clause:

  >>> 
  >>> def CatchingExceptionsCodeBlock():
          try:
              x = int(input('Enter the 1st number: '))
              y = int(input('Enter the 2nd number: '))
              print(x/y)
              print('Happy New Year! This works.') 
          except ZeroDivisionError:                           # except clause 1
              print("ZeroDivision!!! The second number can not be zero.")
          except TypeError:                                   # except clause 2
              print("Dont include text, only numbers please!!!")        
  >>> 
  >>> CatchingExceptionsCodeBlock()
  Enter the 1st number: 25
  Enter the 2nd number: 5
  5.0
  Happy New Year! This works.
  >>> 
  >>> 
  >>> CatchingExceptionsCodeBlock()
  Enter the 1st number: 25
  Enter the 2nd number: 9
  2.7777777777777777
  Happy New Year! This works.
  >>> 
  >>> 
  >>> CatchingExceptionsCodeBlock()
  Enter the 1st number: 25
  Enter the 2nd number: 0
  ZeroDivision!!! The second number can not be zero.      # ok, works so far
  >>> 
  >>> 
  >>> CatchingExceptionsCodeBlock()
  Enter the 1st number: 25
  Enter the 2nd number: hi
  Traceback (most recent call last):
    File "<pyshell#839>", line 1, in <module>
      CatchingExceptionsCodeBlock()
    File "<pyshell#826>", line 4, in CatchingExceptionsCodeBlock
      y = int(input('Enter the 2nd number: '))
  ValueError: invalid literal for int() with base 10: 'hi'        # notice ValueError is NOT
  >>>                                                             # a TypeError so original code
  >>>                                                             # needs refactoring
  >>> CatchingExceptionsCodeBlock()
  Enter the 1st number: 25
  Enter the 2nd number: 'hi'
  Traceback (most recent call last):
    File "<pyshell#842>", line 1, in <module>
      CatchingExceptionsCodeBlock()
    File "<pyshell#826>", line 4, in CatchingExceptionsCodeBlock
      y = int(input('Enter the 2nd number: '))
  ValueError: invalid literal for int() with base 10: "'hi'"
  >>> 


