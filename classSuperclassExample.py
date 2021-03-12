#!usr/bin/env python
# classSuperclassExample.py

>>> class A:
        def hello(self):
            print("Hello, I am A.")

>>> class B(A):
        pass

>>> a = A()
>>> b = B()
>>> 
>>> a.hello()       
Hello, I am A.
>>> b.hello()               # b/c B does not define a hello method of its own
Hello, I am A.              # the original A message is printed in class B.
>>> 

# Now lets add basic functionality in the subclass (ie class B). So lets add methods to the subclass.
# Here B own method will override the superclass's method

>>> class B(A):                         # rebuild class B
        def hello(self):                # add new method
            print("Hello, from B.")     # add new attribute

>>> 
>>> b.hello()                           # call original attribute b.hello (which pulls from class A)
Hello, I am A.
>>> b = B()                             # now rebind b to new class B
>>> b.hello()
Hello, from B.                          # new result!
>>> 
