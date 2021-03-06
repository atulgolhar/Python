# Create your own basic class
# classCreation.py

>>> class Person:
	def set_name(self, name):
		self.name = name
	def get_name(self):
		return self.name
	def greet(self):
		print('Hello world, I am {}'.format(self.name))

		
>>> foo = Person()
>>> bar = Person()
>>> foo.set_name('Luke Skywalker')
>>> bar.set_name('Anakin Skywalker')
>>> 
>>> foo.greet()
Hello world, I am Luke Skywalker
>>> bar.greet()
Hello world, I am Anakin Skywalker
>>> 
>>> Person.greet(foo)
Hello world, I am Luke Skywalker
>>> 
