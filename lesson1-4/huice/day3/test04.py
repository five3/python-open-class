# def add(x, y, f):
#     return f(x) + f(y)
#
def f(x):
    return x**2
#
# print add(2, 3, f)
# print add(2, 3, lambda x:x**2)

number = [1, 2, 3, 4, 5, 6]
# list = map(f, number)
# print list
# print map(lambda x:x**2, number)

# print map(str, number)
#
# name=['xiaoming','xiaohong','xiaofang','xiaogang']
# age=[19,20,21]
# city=['Beijing','Shanghai','Shenzhen','Hangzhou']
# print map(None, name, age, city)
#

# print reduce(lambda x,y:x+y, number)


def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
#
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

def not_empty(list):
    return [s for s in list if s and s.strip()]
