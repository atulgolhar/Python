# exceptionsClausev1.py

# use Python shell

>>> try:
	x = int(input('Enter the first number:'))
	y = int(input('Enter the second number:'))
	print(x/y)
except ZeroDivisionError:
	print("No way Jose")

	
Enter the first number:4
Enter the second number:7
0.5714285714285714

>>> def tryError:
	
SyntaxError: invalid syntax

  >>> def tryError():
		try:
			x = int(input('Enter the first number:'))
			y = int(input('Enter the second number:'))
			print(x/y)
		except ZeroDivisionError:
			print("No way Jose")

			
>>> tryError
<function tryError at 0x7fb2c6c45050>

>>> tryError()
Enter the first number:9
Enter the second number:3
3.0

>>> tryError()
Enter the first number:4
Enter the second number:0
No way Jose
>>> 
