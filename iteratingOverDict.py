#iteratingOverDict.py

>>> d
{'x': 1, 'y': 2, 'z': 3, 'a': 4, 'b': 5, 'c': 6, 'd': 7}

>>> for yyy in d.items():
    print(yyy)
('x', 1)
('y', 2)
('z', 3)
('a', 4)
('b', 5)
('c', 6)
('d', 7)

>>> for zzz in d.keys():
    print(zzz)    
x
y
z
a
b
c
d
>>> 

>>> for xxx in d.values():
    print(xxx)   
1
2
3
4
5
6
7

>>> for key,value in d.items():
    print(key, value)
x 1
y 2
z 3
a 4
b 5
c 6
d 7
>>> 

