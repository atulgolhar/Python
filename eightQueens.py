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
