Generator Methods 
pg 184
# We may supply generators with values after they have started running, by using a communications channel
# between the generator and the "outside world" with the following two end points:
# (1) 'send' method --> the outside world has access to a method on the generator called 'send' 
#     which works just like 'next'
#     except that it 'send' takes a single argument 
#     (the 'message' to send to the generator -- ie 'message' is an arbitrary object).
# (2) 'yield' method inside the suspended generator, 'yield' may now be used as as "expression", 
#     rathar that a "statement"
#     In other words, when the generator is resumed, 'yield' returns a value. 
#     And that value is sent from the outside through 'send'.
#     If 'next' was used, 'yield' returns "None".

# Note that using 'send' (rather than 'next') makes sense only after the generator has been suspended
# (that is, after it has hit the first 'yield').
# If you need to give some information to the generator before that, you can simply use the parameters
# of the generator function.

# TIP If you really want to use 'send' on a newly started generator, you can use it with 'None' as its parameter.
# silly example
# Note use of parentheses are around 'yield' expression.
# While not strictly necessary in some cases, it is probably better to be safe than sorry and thus simply
# always enclose 'yield' expressions in () if you are using the return value in some way

>>> def repeater(value):
          while True:
              new = (yield value)
              if new is not None: value = new
>>> 
>>> r = repeater(42)
>>> next(r)
42
>>> 
>>> r.send("Hello World How Are You?")
'Hello World How Are You?'
>>> 
