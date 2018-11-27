def sum(a, b):
    '''
    :param a: 
    :param b: 
    :return: 
    '''
    print(a+b)

sum(1, 2)
# help(sum)_
print(sum.__doc__)
print(callable(sum))

x = 1
print(callable(x))

import math
def move(x, y, step):
    nx = x + step
    ny = y + step
    return nx, ny

x,y = move(100, 20, 60)
print(x, y)
r = move(100, 20, 60)
print(r)