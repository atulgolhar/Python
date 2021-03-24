Base Case 
pg 188

# base case = last queen
# what to do with her?
# assume you want to find all possible solutions.
# Given this, and given the position of others, 
# you would expect her to generate all the positions she could occupy
# (that could be none)
# you can sketch this out directly:
#       num parameter = number of queens in total
#       state parameter = tuple of positions for previous queens

>>> def queens(num, state):
        if len(state) == num-1:
            for pos in range(num):
                if not conflict(state, pos):
                    yield pos
>>> 

# so                                                index 0 1 2 3 4          _ X _ _
#                                                   row   1 2 3 4 5          _ _ _ X
#                                       quenn(1,3,0)                         X _ _ _ 
#                                       means row 1 col 1                    _ _ I _
#                                             row 2 col 3
#                                             row 3 col 0
# ignore I for now.
# So we look to place a 4th queen. With queens 123 all taking col 1,3,0 respectively, 
# we ask the function to find the 4th queen a slot which has NO conflicts.
        >>> 
        >>> list(queens(4 ,(1,3,0)))
        [2]
        >>> 
# AUTHOR using 'list' simply forces the generator to yield all of its values.
# In this case, only one position qualifies using I in the diagram.


pg 190
# So now you are supplied with one tuple of positions from "above" and 
# for each position of the current queen, you are supplied with a tuple of positions from "below".
# All you need to do to keep things flowing IS TO yield the following result (ie to place)
# "to place" your own psotion ADDED to the FRONT.

""">>> def queens(num, state):
            if len(state) == num-1:
                for pos in range(num):
                    if not conflict(state, pos):
                        yield pos
"""                    
            else:
                for pos in range(num):                  # <<<< identical to above
                    if not conflict(state, pos):        # <<<< identical to above
                        for result in queens(num, state + (pos,)):
                            yield (pos,) + result 

# given "# <<<< identical to above" code, we can rewrite entire code block to simplify
# also adding default arguments as well:

        def queens(num=8, state=()):
            for pos in range(num):
                if not conflict(state, pos):
                    if len(state) == num-1:
                        yield (pos,)
                    else:
                        for result in queens(num, state + (pos,)):
                            yield (pos,) + result

                       
                
>>> 
>>> list(queens(3))
[]
>>> 
>>> list(queens(4))
[(1, 3, 0, 2), (2, 0, 3, 1)]
>>> 
>>> 
>>> list(queens(5))
[(0, 2, 4, 1, 3), (0, 3, 1, 4, 2), (1, 3, 0, 2, 4), (1, 4, 2, 0, 3), 
(2, 0, 3, 1, 4), (2, 4, 1, 3, 0), (3, 0, 2, 4, 1), (3, 1, 4, 2, 0), 
(4, 1, 3, 0, 2), (4, 2, 0, 3, 1)]
>>> 
>>> 
>>> list(queens(6))
[(1, 3, 5, 0, 2, 4), (2, 5, 1, 4, 0, 3), (3, 0, 4, 1, 5, 2), (4, 2, 0, 5, 3, 1)]
>>> 
>>> 
>>> list(queens(7))
[(0, 2, 4, 6, 1, 3, 5), (0, 3, 6, 2, 5, 1, 4), (0, 4, 1, 5, 2, 6, 3), 
(0, 5, 3, 1, 6, 4, 2), (1, 3, 0, 6, 4, 2, 5), (1, 3, 5, 0, 2, 4, 6), 
(1, 4, 0, 3, 6, 2, 5), (1, 4, 2, 0, 6, 3, 5), (1, 4, 6, 3, 0, 2, 5), 
(1, 5, 2, 6, 3, 0, 4), (1, 6, 4, 2, 0, 5, 3), (2, 0, 5, 1, 4, 6, 3), 
(2, 0, 5, 3, 1, 6, 4), (2, 4, 6, 1, 3, 5, 0), (2, 5, 1, 4, 0, 3, 6), 
(2, 6, 1, 3, 5, 0, 4), (2, 6, 3, 0, 4, 1, 5), (3, 0, 2, 5, 1, 6, 4), 
(3, 0, 4, 1, 5, 2, 6), (3, 1, 6, 4, 2, 0, 5), (3, 5, 0, 2, 4, 6, 1), 
(3, 6, 2, 5, 1, 4, 0), (3, 6, 4, 1, 5, 0, 2), (4, 0, 3, 6, 2, 5, 1), 
(4, 0, 5, 3, 1, 6, 2), (4, 1, 5, 2, 6, 3, 0), (4, 2, 0, 5, 3, 1, 6), 
(4, 6, 1, 3, 5, 0, 2), (4, 6, 1, 5, 2, 0, 3), (5, 0, 2, 4, 6, 1, 3), 
(5, 1, 4, 0, 3, 6, 2), (5, 2, 0, 3, 6, 4, 1), (5, 2, 4, 6, 0, 3, 1), 
(5, 2, 6, 3, 0, 4, 1), (5, 3, 1, 6, 4, 2, 0), (5, 3, 6, 0, 2, 4, 1), 
(6, 1, 3, 5, 0, 2, 4), (6, 2, 5, 1, 4, 0, 3), (6, 3, 0, 4, 1, 5, 2), 
(6, 4, 2, 0, 5, 3, 1)]
>>>
>>> len(list(queens(3)))
0
>>> len(list(queens(4)))
2
>>> len(list(queens(5)))
10
>>> len(list(queens(6)))
4
>>> len(list(queens(7)))
40
>>> len(list(queens(8)))        # from AUTHOR (ATUL did not run this)
92


Wrapping It Up

# before leaving the queens, lets make the output a bit more understandable.
# Clear output is always good and makes it easier to spot bugs.
# AUTHOR made a helper function inside 'prettyprint'
# why? its inside 'prettyprint' b/c the AUTHOR assumed he would not need it anywhere else outside.
# Now lets print the solution to satisfy myself that it is correct.

>>> 
>>> def prettyprint(solution): 
        def line(pos, length=len(solution)):                        # helper function
            return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
        for pos in solution:
            print(line(pos))

>>> import random
>>> prettyprint(random.choice(list(queens(5))))
. . . X . 
X . . . . 
. . X . . 
. . . . X 
. X . . . 
>>> 
>>> prettyprint(random.choice(list(queens(4))))
. . X . 
X . . . 
. . . X 
. X . . 
>>> 
>>> prettyprint(random.choice(list(queens(7))))
. . X . . . . 
. . . . . . X 
. X . . . . . 
. . . X . . . 
. . . . . X . 
X . . . . . . 
. . . . X . . 
>>> 

