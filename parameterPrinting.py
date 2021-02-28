# Example of parameter printing, formatting

>>> def print_params_2(title, *params):
      print(title)
      print(params)

  >>> print_params_2('Params:',1,2,3)
  Params:
  (1, 2, 3)


  >>> def print_params_2a(title, *params):
      print(titlleeee)                            # notice that the name can be anything
      print(params)

  >>> print_params_2('Params:',1,2,3)
  Params:
  (1, 2, 3)

  >>> def print_params_2a(title, *params):
      print(titlsfsdfsadfasdf)                    # notice that the name can be anything
      print(params)

  >>> print_params_2('Params:',1,2,3)
  Params:
  (1, 2, 3)

  >>> print_params_2('Params:',1,2,3,5,345,35,45456,456)
  Params:                                                 # <<<<<<<<< notice the title is here
  (1, 2, 3, 5, 345, 35, 45456, 456)

  >>> print_params_2(1,2,3,5,345,35,45456,456, 'Params')
  1                                                       # <<<<<<<<<<< notice the title is here
  (2, 3, 5, 345, 35, 45456, 456, 'Params')

  >>> print_params_2('Nothing:')
  Nothing:
  ()
  >>> print_params_2('Nothing:',       )
  Nothing:
  ()
